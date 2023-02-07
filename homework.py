from pymongo import MongoClient,ASCENDING
from dotenv import load_dotenv
import os 
import urllib
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
load_dotenv('.env')

user = (os.getenv('username'))
password = urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')

print(client.list_database_names())
db = client["exceed04"] 
colletion = db['lockers']

app = FastAPI()
z = []
@app.get("/lockers")
def root():
    for x in colletion.find({},{"_id":0,"id" : 1 ,"available" : 1 ,"end_time": 1  }):
        print(x)
        if x["available"] == True :
            x.pop("end_time")
        
        z.append(x)
    return z
    