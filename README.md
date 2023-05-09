# streaming_data_pipeline
This repository contains scripts to building stock market streaming data pipeline. 

# Abstract
The need for building streaming data pipelines for getting, processing, and analysing data efficiently once it is generated grows in a fast manner. With an increase in demand for fast generation of useful insights, technologies and methods contributing to it develop as well. In the scope of this project, our aim was building a real-time data streaming pipeline while exploring different approaches and the available tools and technologies.

# Requirements
To have the necessary libraries run the following code:

pip install -r requirements.txt

# Flow
Please, make the required changes to the configs.py and make sure to utilize your Google Drive and Cloud login information.

Run the infrastructure_initiation.py file only once. 

Note that Kafka runs on Confluent Cloud.

Run the consumer file as follows: python ./consumer.py getting_started.ini

Run the producer file as follows: python ./producer.py getting_started.ini

# Usage
To use this repository, you can clone it to your local machine: git clone https://github.com/KristineManukyan/streaming-data-pipeline.git

# Keywords
Apache Kafka, Python, BigQuery
