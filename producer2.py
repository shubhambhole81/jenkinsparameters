from kafka import KafkaProducer
from json import dumps
from jsonfun import *

KAFKA_URL = 'localhost:9092' # kafka broker
KAFKA_TOPIC = 'jenkins-stage' # topic name

producer = KafkaProducer(bootstrap_servers=[KAFKA_URL], value_serializer = lambda x:dumps(x).encode('utf-8'))
 
try:
    producer.send(KAFKA_TOPIC, value = pipeline_info())
    producer.flush()
    for df in stage_info():
        producer.send(KAFKA_TOPIC, value = df)
        producer.flush() # immediately available the buffer messages to send further.
        
         
except Exception as e:
    print("NO Broker Available.......")
