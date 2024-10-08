from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os
from werkzeug.datastructures import MultiDict

load_dotenv()

# Assuming your MongoDB connection string is stored in the environment variable 'MONGODB_URI'
mongo_uri = os.environ.get('MONGODB_URI')
client = MongoClient(mongo_uri)

# Select your database and collection
db = client.get_database("career")


def sign_in(form_data):
    data = MultiDict(form_data)
    users_collection = db['users']
    user = users_collection.find_one({'email': data['email']})
    print(user)
    if user:
        return True
    return False


def load_jobs():
    collection = db["jobs"]
    # Find all documents in the 'jobs' collection
    jobs = list(collection.find())
    return jobs


def get_job_by_id(job_id):
    collection = db['jobs']
    try:
        obj_id = ObjectId(job_id)
    except:
        return None
    job = collection.find_one({"_id": obj_id})
    if not job:
        return None
    return job


def apply_job(jobid, form_data):
    collection_jobs = db['jobs']
    job = collection_jobs.find_one({'_id': ObjectId(jobid)})

    if not job:
        return "Not Found"
    else:
        # Convert the ImmutableMultiDict to a mutable MultiDict
        data = MultiDict(form_data)
        # Add job_id to the application data
        data.add("job_id", ObjectId(jobid))
        data.add("_id", ObjectId())
        data_dict = dict(data)
        # Convert the dictionary to JSON
        # json_data = json.dumps(data_dict, indent=2)

        collection_applications = db['applications']
        response = collection_applications.insert_one(data_dict)
        return response.inserted_id


def get_applications_by_job_id(job_id):
    collection = db['applications']
    try:
        obj_id = ObjectId(job_id)
    except:
        return None
    applications = list(collection.find({"job_id": obj_id}))
    return applications
