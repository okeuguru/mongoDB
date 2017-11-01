#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
grades = db.grades


def find():
    print ("find, reporting for duty")
    query = {"type":"exam", 'score': {"$gte": 65}}
    try:
        cursor = grades.find(query)
        #cursor.limit(1)
        cursor.sort('score', pymongo.ASCENDING).limit(1)
        #cursor.sort([('student_id', pymongo.ASCENDING),('score', pymongo.DESCENDING)])

    except Exception as e:
        print ("Unexpected error:", type(e), e)

    for doc in cursor:
        print (doc)


if __name__ == '__main__':
    find()
