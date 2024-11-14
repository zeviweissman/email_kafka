import email_producer.app.utils.email_utils as u
import email_producer.app.producer.email_producer as email_producer

def produce_email(email):
    email_producer.all_email_producer(email)

    if u.email_contains_hostage(email['sentences']):
        email_producer.hostage_email_producer(email)

    if u.email_contains_explosive(email['sentences']):
        email_producer.explosive_email_producer(email)