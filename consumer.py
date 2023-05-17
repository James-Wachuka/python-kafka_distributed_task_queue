import logging
from kafka import KafkaConsumer, KafkaProducer

# Kafka configuration
bootstrap_servers = 'localhost:9092'
task_topic = 'task_topic'
result_topic = 'result_topic'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Kafka consumer and producer
consumer = KafkaConsumer(task_topic, bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Process tasks
for message in consumer:
    task = message.value.decode('utf-8')
    logger.info(f'Received task: {task}')
    
    # Perform task processing logic here
    result = task.upper()  # Example: Uppercase the task
    logger.info(f'Processed task: {task} --> Result: {result}')

    # Send the result to the result topic
    producer.send(result_topic, result.encode('utf-8'))
    producer.flush()
    logger.info(f'Result sent to {result_topic}')
