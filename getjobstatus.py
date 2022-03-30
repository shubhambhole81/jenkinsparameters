#import os
#print("JOB_NAME: ",os.environ['JOB_NAME'])
#print("JOB-BUILD_NUMBER: ",os.environ['BUILD_NUMBER'])
#print("JOB-BUILD_URL: ",os.environ['BUILD_URL'])
#print("JOB-BUILD_TAG: ",os.environ['BUILD_TAG'])
import requests
url = "https://http://localhost:8080/job/TestPipeline//lastBuild/wfapi/"
response = requests.request("GET", url,auth=('dharmendra','Kumar@123'))
data = response.json()
print (data['stages'])
print (data['id'])
print (data['status'])
