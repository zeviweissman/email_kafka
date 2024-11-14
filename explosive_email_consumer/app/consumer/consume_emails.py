import os
from email_kafka.kafka_connection.consumer import consume
import explosive_email_consumer.app.service.email_service as email_service

explosive_topic = os.environ['EXPLOSIVE_TOPIC']


def consume_emails():
    consume(
        topic=explosive_topic,
        function=email_service.insert_email,
    )