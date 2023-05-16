from kafka import KafkaConsumer, KafkaProducer

# Kafka configuration
bootstrap_servers = 'localhost:9092'
task_topic = 'task_topic'
result_topic = 'result_topic'

# Create Kafka consumer and producer
consumer = KafkaConsumer(task_topic, bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Process tasks
for message in consumer:
    task = message.value.decode('utf-8')
    # Perform task processing logic here
    result = task.upper()  # Example: Uppercase the task

    # Send the result to the result topic
    producer.send(result_topic, result.encode('utf-8'))
    producer.flush()
    
