from lesson_26.base_db_client import BaseClient


class HotelsCollection(BaseClient):
    def __init__(self, collection_name, db_name='hotels'):
        super().__init__(db_name)
        self.collection_name = collection_name
        self.db_name = db_name

    def insert_hotel(self, hotel_data):
        """
        Inserts a single hotel into the collection
        :param hotel_data: a dictionary containing the data for the hotel document
        """
        result = self.insert_one(self.collection_name, hotel_data)
        return result.inserted_id

    def insert_hotels(self, hotels_data):
        """
        Inserts multiple hotel documents into the collection.
        :param hotels_data: a list of dictionaries, each containing the data for a hotel document
        """
        result = self.insert_many(self.collection_name, hotels_data)
        return result.inserted_ids

    def find_one_by_name(self, name):
        query = {'name': name}
        return self.find_one(self.collection_name, query)

    def find_many_by_location(self, location):
        query = {'location': location}
        cursor = self.db[self.collection_name].find(query)
        return list(cursor)  # return cursor object as a list for futher manipulations

    def find_all_hotels(self):
        query = {}
        cursor = self.db[self.collection_name].find(query)
        return list(cursor)  # return cursor object as a list for futher manipulations

    def find_many_by_rating(self, min_rating):
        query = {'rating': {'$gte': min_rating}}
        cursor = self.db[self.collection_name].find(query)
        return list(cursor)

    def delete_one_hotel_by_id(self, hotel_id):
        filter_query = {'_id': hotel_id}
        return self.delete_one(self.collection_name, filter_query)

    def delete_all_hotels(self):
        filter_query = {}
        return self.delete_many(self.collection_name, filter_query)

    # def get_distinct_location_names(self):
    #     return self.distinct(self.collection_name, 'location')
