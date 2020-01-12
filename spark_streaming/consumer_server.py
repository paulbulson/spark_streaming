from kafka import KafkaConsumer
from json import loads

# Based on article
# https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

consumer = KafkaConsumer(
    'calls',
    group_id = '0',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{} consumed'.format(message))
