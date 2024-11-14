import os
from email_kafka.kafka_connection.consumer import consume
import hostage_email_consumer.app.service.email_service as email_service

hostage_topic = os.environ['HOSTAGE_TOPIC']


def consume_emails():
    consume(
        topic=hostage_topic,
        function=email_service.insert_email,
    )