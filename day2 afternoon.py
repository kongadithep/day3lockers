from pymongo import MongoClient,ASCENDING
from dotenv import load_dotenv
import os 
import urllib
load_dotenv('.env')

user = (os.getenv('username'))
password = urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')

print(client.list_database_names())
db = client["exceed04"] 
colletion = db['exceed']
'''
{
    stdId: int,
    stdName:str,
    course_name:string,
    grade: number,
    unit:number
}
'''
res = colletion.insert_many([{"person":"1"},{'person':"2"}])

finsert = colletion.insert_one({
    "stdId":2468,
    "stdName":"kong",
    "course_name": "exceed",
    "grade" : 4.00,
    "unit" : 3,   
})
print(colletion.find_one())
# res = colletion.insert_many()

colletion.update_one({'stdId':'6410545797'},{'$set':{'grade':4}},upsert=True)

# for i in colletion.find():
#     print(i)

# ori_data = colletion.find({'course_name':'hello'})
# if ori_data:
#     print("Not_Found")

