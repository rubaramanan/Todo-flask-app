import yaml
import uuid
from pymongo import MongoClient
from bson.json_util import dumps

class user():

    def __init__(self):
        self.mongoclient = MongoClient('mongodb://localhost:27017/')
        self.db = self.mongoclient.users
        self.collection = self.db.user

    def create_user(self, user_dic):
        user_dic['_id'] = str(uuid.uuid4())
        user = self.collection.insert_one(user_dic).inserted_id
        # print(list(user))
        return user_dic
            

    def get_users(self):
         users = self.collection.find()  
         users = list(users)
         return users

    def get_user(self, id):
        user = self.collection.find_one({"_id": id})
        print(user)
        return user


    def modify_user(self, id, update_dic):
        self.collection.update_one({"_id": id}, {"$set": update_dic})

    def delete_user(self, id):
        self.collection.delete_one({"_id": id})    