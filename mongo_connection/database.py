from pymongo import MongoClient
import os


def get_mongo_client():
    return MongoClient(os.environ['MONGO_URL'])

def get_emails_collection():
    db = get_mongo_client()['army']
    return db['emails']

