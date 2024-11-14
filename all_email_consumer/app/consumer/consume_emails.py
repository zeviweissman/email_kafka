import os

from email_kafka.kafka_connection.consumer import consume
import all_email_consumer.app.service.email_service as email_service

all_email_topic = os.environ['ALL_EMAIL_TOPIC']


def consume_emails():
    consume(
        topic=all_email_topic,
        function=email_service.add_email,
    )