'''
Methods for interacting with the noSQL database
'''
import pymongo

def connect_to_database(database_name):
    db_user = 'andrew'
    db_password = 'Parkdale24'
    mongodb_uri = 'mongodb://andrew:Parkdale24@ds129541.mlab.com:29541/tweets01'

    client = pymongo.MongoClient(mongodb_uri)
    return client[database_name]

def insert_single(database_connection, collection, document):
    collection = database_connection[collection]
    collection.insert_one(document)
