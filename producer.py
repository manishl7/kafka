from kafka import KafkaProducer
import json
from data import get_registered_user
import time

def json_serializer(data):#when this runs ,it'll get the data
    return(json.dumps(data).encode('utf-8')) #to make sure when we are deserializing all the texts are in utf-8

producer=KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],value_serializer=json_serializer)

if __name__=='__main__':
    while 1==1: #running an infinite loop
        registered_user=get_registered_user()
        #this will also print the data before being sent
        print(registered_user)
        #while sending data we'll need to send topic name as well
        producer.send('kafka-project',registered_user)
        #this will publish a record after every 4 seconds
        time.sleep(4)