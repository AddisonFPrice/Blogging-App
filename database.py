import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017"
    database = None

    @staticmethod
    def connect(self):
        client = pymongo.MongoClient(Database.URI)
        database = client['db1']

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)

    @staticmethod
    def insert(collection, data):
        return Database.database[collection].insert(data)