from all_email_consumer.app.consumer.consume_emails import consume_emails
from dotenv import load_dotenv

load_dotenv(verbose=True)

if __name__ == '__main__':
    consume_emails()