import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

try:
    status = requests.get('http://localhost:8080/job/TestPipeline/lastBuild/wfapi/', auth=HTTPBasicAuth('dharmendra', 'Kumar@123'))
    
    status.raise_for_status() #raise exception for error code. 

    # return json object.
    data=status.json()


    def pipeline_info():
        build_no=data["name"]
        build_status=data['status']
        pipeline_startime=datetime.fromtimestamp(data['startTimeMillis']//1000).isoformat()
        pipeline_endtime=datetime.fromtimestamp(data['endTimeMillis']//1000).isoformat()
        pipeline_duration=data['durationMillis']
        
        
        build_pipeline_data= { "Build_number": build_no,"build_status":build_status,"pipeline_startime":pipeline_startime," pipeline_endtime": pipeline_endtime,
                                 "pipeline_duration":pipeline_duration
                            }
    
        return  build_pipeline_data

    def stage_info():
        stage_data = []
    # Extarcting the data from json and saving it to dictonary.    
        for key in data['stages'][1:]:
            StageName = key['name']
            EndTime1 = key['startTimeMillis']+ key['durationMillis']
            EndTime= datetime.fromtimestamp(EndTime1//1000).isoformat()
            StartTime = datetime.fromtimestamp(key['startTimeMillis']//1000).isoformat()
            DurationTime = key['durationMillis']
            status= key['status']

            dta = {"Stage_Name":StageName, "StartTime": StartTime, "EndTime": EndTime, "DurationTime": DurationTime,"Stage_status":status }
            # appending all stages of pipeline to list.
            stage_data.append(dta)
        return stage_data
    
except requests.exceptions.HTTPError: # handle exception for invalid url.
        print("Enter valid url..")
    
