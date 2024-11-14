from dotenv import load_dotenv
from explosive_email_consumer.app.consumer.consume_emails import consume_emails
from psql.psql_functions import initate_db, drop_data_base_if_exists

load_dotenv(verbose=True)


if __name__ == '__main__':
    #drop_data_base_if_exists()
    initate_db()
    consume_emails()