from mongo_connection.database import get_emails_collection

emails_collection = get_emails_collection()

def insert_email(email_to_add):
    email = emails_collection.insert_one(email_to_add)
    return email.inserted_id
