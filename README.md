# Distributed Task Queue with Kafka

This project demonstrates a simple implementation of a distributed task queue using Apache Kafka. It consists of two components: a task producer that enqueues tasks and a worker consumer that processes the tasks.

## Prerequisites

- Apache Kafka: Download and install Apache Kafka on your local machine or a server. You can find the Kafka downloads and installation instructions on the [Apache Kafka website](https://kafka.apache.org/downloads).
- Python: Make sure you have Python installed on your system.

## Setup and Usage -python virtual environment
- clone the repository
1. download and extract kafka
2. build the kafka project -inside the kafka folder run ```./gradlew jar -PscalaVersion=2.13.10```
3. Start ZooKeeper: ```bin/zookeeper-server-start.sh config/zookeeper.properties```
4. start kafka brokers: ```bin/kafka-server-start.sh config/server.properties```
5. install kafka-python
6. create kafka topics:
    ```bin/kafka-topics.sh --create --topic task_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1```
    ```bin/kafka-topics.sh --create --topic result_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1```
7. run ```consumer.py``` and ```producer.py``` in separate terminals
8. Verify Output: The consumer will process the tasks produced by the producer and print the results to the console.

## Customization

- Task Processing Logic: Customize the task processing logic in the `consumer.py` file according to your specific requirements. The provided example simply converts the tasks to uppercase. Here is the enhanced [consumer code](consumer.py) 

- Scaling: You can scale the worker consumer by running multiple instances of the consumer code on different machines or processes. Kafka's distributed nature enables efficient load balancing across multiple consumers.

- Error Handling: Enhance the code with error handling mechanisms, such as retrying failed tasks, logging errors, or sending alerts in case of task failures. [This consumer and producer code](consu_prod.py) has been improved for error handling

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).




