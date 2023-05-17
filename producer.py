from kafka import KafkaProducer

# Kafka producer configuration
bootstrap_servers = 'localhost:9092'
task_topic = 'task_topic'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Enqueue tasks
tasks = ['task1', 'task2', 'task3']  # Example tasks
for task in tasks:
    # Enqueue the task to the task topic
    producer.send(task_topic, task.encode('utf-8'))
    producer.flush()
    print(f"Task enqueued: {task}")

# Close the producer connection
producer.close()
