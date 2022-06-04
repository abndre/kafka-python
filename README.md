# Kafka + Python

This Project uses Kafka message Broker and two python scripts to be the consumer and producer.

## Architecture

```
            kafdrop (web)
              |
producer >> kafka >> consumer
              |
            zookeper
```

The Kafdrop is a web application to see the Kafka message and topcs.
The producer and consumer is writen with python

## Deploy

Run the compose with

```
docker-compose up
```

Access the [KAFDROP WEB](http://localhost:19000), is possible to creat a topic and see messages by this web app.


## Installation 

For run python consumer and producer install kafka-python

```
pip3 install kafka-python
```

### Consumer

Run the consumer using
```
python3 consumer_kafka.py
```

### Producer

Run the producer using
```
python3 producer_kafka.py
```