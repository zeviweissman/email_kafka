import psql.repository.email_repository as email_repos
import explosive_email_consumer.app.utils.convert_utils as convert_utils


def insert_email(kafka_email):
    email = kafka_email.value
    email_model = convert_utils.convert_json_to_email_model(email)
    email_repos.insert_email(email_model)