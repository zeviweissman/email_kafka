import os

from email_kafka.kafka_connection.producer import produce


all_email_topic = os.environ['ALL_EMAIL_TOPIC']
hostage_topic = os.environ['HOSTAGE_TOPIC']
explosive_topic = os.environ['EXPLOSIVE_TOPIC']

def all_email_producer(email):
    produce(
        topic=all_email_topic,
        key=email['id'],
        value=email
    )
    print("produced to all email topic")

def hostage_email_producer(email):
    produce(
        topic=hostage_topic,
        key=email['id'],
        value=email
    )
    print("produced to hostage email topic")


def explosive_email_producer(email):
    produce(
        topic=explosive_topic,
        key=email['id'],
        value=email
    )
    print("produced to explosive email topic")
