from confluent_kafka.admin import AdminClient, NewTopic

# Initialize Kafka AdminClient
admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

# Specify the topic to delete
topic_name = 'color-topic'

# Delete the topic
fs = admin_client.delete_topics([topic_name], operation_timeout=30)
try:
    fs[topic_name].result()
    print(f"Topic {topic_name} deleted successfully.")
except Exception as e:
    print(f"Failed to delete topic {topic_name}: {e}")
