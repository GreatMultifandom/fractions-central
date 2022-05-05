from pymongo import MongoClient
import config

class Database:
    def __init__(self):
        self.db = MongoClient(config.mongo_url)
        self.fractions = self.db.fractions