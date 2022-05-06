from pymongo import MongoClient
import config

class Database:
    def __init__(self):
        self.db = MongoClient(config.mongo_url).fractions
        self.chats = self.db.chats
    
    def get_chats(self):
        return self.chats.find({})

    def add_chat(self, name, chat_id):
        return self.chats.insert_one({
            'fraction': name,
            'id': chat_id
        })
        