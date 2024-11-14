import all_email_consumer.app.repository.email_repository as email_repos


def add_email(kafka_email):
    email_repos.insert_email(kafka_email.value)
