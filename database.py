from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

# Assuming your MongoDB connection string is stored in the environment variable 'MONGODB_URI'
mongo_uri = os.environ.get('MONGODB_URI')
client = MongoClient(mongo_uri)

# Select your database and collection
db = client.get_database("career")


def load_jobs():
    print("Connected to Data Base")
    collection = db["jobs"]
    # Find all documents in the 'jobs' collection
    jobs = list(collection.find())
    return jobs


def get_job_by_id(job_id):
    obj_id = ObjectId(job_id)
    collection = db['jobs']
    job = collection.find_one({"_id": obj_id})
    if not job:
        return None
    return job


# print(get_job_by_id("65a4483753d7e44af4b59ac7"))
