from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Assuming your MongoDB connection string is stored in the environment variable 'MONGODB_URI'
mongo_uri = os.environ.get('MONGODB_URI')
client = MongoClient(mongo_uri)

# Select your database and collection
db = client.get_database("career")
collection = db["jobs"]


def load_jobs():
    # Find all documents in the 'jobs' collection
    jobs = list(collection.find())
    return jobs
