#simple kafka project that streams data.py 

1>need to create a topic for the same. In my case topic = kafka-topic

2>Start zookeeper server and kafka server 
2.1>To start zookeper server
zookeeper-server-start.sh config/zookeper.properties 
2.2>To start kafka server
kafka-server-start.sh config/server.properties

3>To create a topic
kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic kafka-project --create   #kafka-proect is just the name of the topic ;it can be anything.
then 3.1>to run consumer #this is where we can view results
kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9002 --topic kafka-project 

4>Once the kafka topic is creaated run the data.py and producer.py

Requirements:

pip install kafka-python
pip install faker # to generate random data

sudo apt install default -jre
sudo apt install default -jdk

go to kafka.apache.org/downloads
then binary downloads then scala 2.13 copy link address
go to terminal
wget (pastethelink)

extract the content of the zip file 
tar -xvf kafka_2.3.......
cd kafka

you can run the file using
bin/kafka-topics.sh

