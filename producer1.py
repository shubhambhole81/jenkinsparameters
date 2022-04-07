import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from kafka import KafkaProducer
from json import dumps
import time

KAFKA_URL = 'localhost:9092' # kafka broker
KAFKA_TOPIC = 'jenkins-stage' # topic name
 
try:
    # authenticate request from jenkins api.
    status = requests.get('http://localhost:8080/job/TestPipeline/lastBuild/wfapi/', auth=HTTPBasicAuth('dharmendra', 'Kumar@123'))
    
    status.raise_for_status() #raise exception for error code. 
    
    producer = KafkaProducer(bootstrap_servers=[KAFKA_URL], value_serializer = lambda x:dumps(x).encode('utf-8'))
    
    # return json object.
    data=status.json()
    build_no=data["name"]
    build_status=data['status']
    pipeline_startime=datetime.fromtimestamp(data['startTimeMillis']//1000).isoformat()
    pipeline_endtime=datetime.fromtimestamp(data['endTimeMillis']//1000).isoformat()
    pipeline_duration=(data['durationMillis']//1000)//60
    
    fdata= { "Build_number": build_no,"build_status":build_status,"pipeline_startime":pipeline_startime," pipeline_endtime": pipeline_endtime,
                 "pipeline_duration":pipeline_duration
            } 

    producer.send(KAFKA_TOPIC, value = fdata)
    producer.flush()
    
    # Extarcting the data from json and saving it to dictonary. 
    for key in data['stages']:
        StageName = key['name']
        EndTime1 = key['startTimeMillis']+ key['durationMillis']
        EndTime= datetime.fromtimestamp(EndTime1//1000).isoformat()
        StartTime = datetime.fromtimestamp(key['startTimeMillis']//1000).isoformat()
        DurationTime = (key['durationMillis']//1000)//60
        status= key['status']
            
        f1data = {"Stage_Name":StageName, "StartTime": StartTime, "EndTime": EndTime, "DurationTime": DurationTime,"Stage_status":status }
        producer.send(KAFKA_TOPIC, value = f1data)
            
        #time.sleep(5) 
        producer.flush() # immediately available the buffer messages to send further.
        
         
except requests.exceptions.HTTPError: # handle exception for invalid url.
    print("Enter valid url..")
except Exception as e:
    print("NO Broker Available.......")   
        



