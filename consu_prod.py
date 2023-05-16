from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
import traceback

# Kafka configuration
bootstrap_servers = 'localhost:9092'
task_topic = 'task_topic'
result_topic = 'result_topic'

# Create Kafka consumer and producer
consumer = KafkaConsumer(task_topic, bootstrap_servers=bootstrap_servers,
                         enable_auto_commit=False, auto_offset_reset='earliest')
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Process tasks
for message in consumer:
    task = message.value.decode('utf-8')
    try:
        # Perform task processing logic here
        result = task.upper()  # Example: Uppercase the task

        # Send the result to the result topic
        producer.send(result_topic, result.encode('utf-8')).add_callback(
            lambda m: print(f"Task '{task}' processed successfully and result sent to the result topic.")
        ).add_errback(
            lambda e: print(f"Failed to send result for task '{task}'. Error: {e}")
        )

        # Commit the offset to mark the task as processed
        consumer.commit()

    except Exception as e:
        print(f"Error occurred while processing task '{task}': {e}")
        # Optionally, you can handle or log the error here

consumer.close()
producer.close()

'''
To add error handling and task acknowledgement to the Kafka implementation, 
you can make use of Kafka's message acknowledgment feature 
and handle any potential exceptions that may occur during processing
We set enable_auto_commit=False when creating the Kafka consumer to disable automatic offset commits. 
This allows us to manually commit the offset only after successfully processing a task.
After processing a task, we use the add_callback() method on the Kafka producer's send() call to add a callback function that will be executed when the result is successfully sent to the result topic. 
In the callback, we print a success message indicating that the task was processed and the result was sent.
We also use the add_errback() method to add an error callback function that will be executed if there is an error while sending the result to the result topic. 
In the error callback, we print an error message indicating the failure.
After sending the result and before committing the offset, we explicitly call consumer.commit() to manually commit the offset, marking the task as processed.

'''
