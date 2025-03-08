import random
import json
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError  # Import KafkaError for error handling

colors = ['red', 'blue', 'green', 'yellow']

# Connect to Kafka broker
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def generate_message():
    color = random.choice(colors)
    value = random.randint(1, 100)
    message = {
        'color': color,
        'value': value
    }
    return message

while True:
    message = generate_message()
    
    try:
       
        producer.send('color-topic', json.dumps(message).encode('utf-8')).get(timeout=10)
        print(f"Sent: {message}")
    except KafkaError as e:
        print(f"Error while sending message: {e}")
    
    time.sleep(10)  

