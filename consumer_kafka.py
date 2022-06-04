from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'hello_topic',
     bootstrap_servers=['localhost:9092'],
     value_deserializer=lambda x: loads(x.decode('utf-8')))
    #  auto_offset_reset='earliest',
    #  enable_auto_commit=True,
    #  group_id='my-group',
    #  value_deserializer=lambda x: loads(x.decode('utf-8')))

soma = 0
for value in consumer:
    soma += float(value.value)
    print(value.value, soma)