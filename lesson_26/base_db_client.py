import pymongo
from lesson_26 import config_reader


class BaseClient:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient(config_reader.get_connection())
        self.db = self.client[db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_many(data)

    def find_one(self, collection_name, search_query):
        collection = self.db[collection_name]
        return collection.find_one(search_query)

    def find(self, collection_name, search_query):
        collection = self.db[collection_name]
        return collection.find(search_query)

    def update_one(self, collection_name, _filter: dict, update: dict, upsert=False):
        collection = self.db[collection_name]
        return collection.update_one(_filter, update, upsert=upsert)  # if upsert flag is set to True - new document
        # will be inserted if no documents match the filter criteria

    def update_many(self, collection_name, _filter: dict, update: dict, upsert=False):
        collection = self.db[collection_name]
        return collection.update_many(_filter, update, upsert=upsert)  # if upsert flag is set to True - new document
        # will be inserted if no documents match the filter criteria

    def delete_one(self, collection_name, _filter: dict):
        collection = self.db[collection_name]
        return collection.delete_one(_filter)

    def delete_many(self, collection_name, _filter: dict):
        collection = self.db[collection_name]
        return collection.delete_many(_filter)

    def distinct(self, collection_name, filter_key: str, query=None):
        collection = self.db[collection_name]
        return collection.distinct(filter_key, filter=query)
