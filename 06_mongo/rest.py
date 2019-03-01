#theLins: Susan and Vincent
#SoftDev2 pd08
#K #06: Yummy Mongo Py
#F 2019-03-01

from pymongo import MongoClient

SERVER_ADDR = "206.189.205.115"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

def borough(name):
    return collection.find("borough":name)

def zip(num):
    return collection.find("address.zipcode":num)

def zipGrade(zip, grade):
    return collection.find("address.zipcode":num, "grades.grade":grade)

def zipThreshold(zip, thresh):
    return collection.find("address.zipcode":num, 'grades.score':{'$lt': thresh})
