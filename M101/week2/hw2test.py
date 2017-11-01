#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
grades = db.grades


def find_student_data():
    # get a handle to the school database
    db = connection.students
    grades = db.grades


    try:
        student_id = 0
        while student_id < 200:
            print ("Searching for student data for student with id = ", student_id)
            docs = grades.find({'type':'homework','student_id':student_id}).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)]).limit(1)
            print('deleting lowest hw for id', student_id)
            for doc in docs:
                grades.delete_many(doc)
                print ('deleted')
            student_id +=1

    except Exception as e:
        print ("Exception: ", type(e), e)

find_student_data()
