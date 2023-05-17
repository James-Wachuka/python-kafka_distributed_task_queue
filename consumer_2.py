import time
from kafka import KafkaConsumer

# Kafka configuration
bootstrap_servers = 'localhost:9092'
task_topic = 'task_topic'
result_topic = 'result_topic'

# Create Kafka consumer
consumer = KafkaConsumer(task_topic, bootstrap_servers=bootstrap_servers)

# Start consuming messages
for message in consumer:
    task = message.value.decode('utf-8')
    print(f"Received task: {task}")
    
    # Simulate time-consuming task processing
    time.sleep(5)  # Delay of 5 seconds
    
    # Perform task processing logic here
    result = task.upper()  # Example: Uppercase the task

    # Send the result to the result topic
    print(f"Task processed: {task} --> Result: {result}")


'''
In this updated code, we've added a time.sleep(5) statement to simulate a time-consuming task that takes 5 seconds to process. 
You can modify the sleep duration to match your desired processing time.
With this enhancement, each task received by the worker will undergo a delay of 5 seconds before processing. 
This can simulate scenarios where tasks require significant computation or external resource access.
'''