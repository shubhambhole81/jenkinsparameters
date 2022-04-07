import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time

KAFKA_URL = 'localhost:9092' # kafka broker
KAFKA_TOPIC = 'jenkins-stage' # topic name
 
try:
    # authenticate request from jenkins api.
    status = requests.get('http://localhost:8080/job/TestPipeline/lastBuild/wfapi/', auth=HTTPBasicAuth('dharmendra', 'Kumar@123'))
    
    status.raise_for_status() #raise exception for error code. 
    
    # return json object.
    data=status.json()
    
    # Extarcting the data from json and saving it to dictonary. 
    for key in data['stages']:
        StageName = key['name']
        EndTime1 = key['startTimeMillis']+ key['durationMillis']
        EndTime= datetime.fromtimestamp(EndTime1//1000).isoformat()
        StartTime = datetime.fromtimestamp(key['startTimeMillis']//1000).isoformat()
        DurationTime = (key['durationMillis']//1000)//60
            
        fdata = {"Stage_Name":StageName, "StartTime": StartTime, "EndTime": EndTime, "DurationTime": DurationTime}
        
        try:    
            producer = KafkaProducer(bootstrap_servers=[KAFKA_URL], value_serializer = lambda x:dumps(x).encode('utf-8'))
            producer.send(KAFKA_TOPIC, value = fdata)
            #time.sleep(5) 
            producer.flush() # immediately available the buffer messages to send further.
        
        except Exception as e:
            print("NO Broker Available.......") 
            
except requests.exceptions.HTTPError: # handle exception for invalid url.
    print("Enter valid url..")
        



