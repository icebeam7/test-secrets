# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo 


def aws_upload(data: Dict):
    database = aws_lib.connect("test", "test2")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb://admin:password@localhost:27017/db"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
