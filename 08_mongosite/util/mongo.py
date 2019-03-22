# Team Curved Windows -- Joyce Liao, Susan Lin
# Softdev2 pd8
# K07 -- Import/Export Bank
# 2019-03-03

# Dataset: /r/todayilearned - information such as upvotes and comments on posts in the 'todayilearned' subreddit
# Raw data at https://www.reddit.com/r/todayilearned.json
# Note on importing:
# Open raw data in a text editor
# Remove all content from the beginning of file up to the first "["
# Navigate to the end of file
# Remove all content from the very last "]" to the end of file
# Now the file should contain only an array of json data, save file
# When running $mongoimport, add the --jsonArray flag

import pymongo, json

SERVER_ADDR = "159.65.234.2"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.curved_windows
collection = db.til

def connect(address, port=27017):
    client = MongoClient(address, port)
    return client

def getdb(client, name):
	db = client[name]
	return db

def getcollection(db, name):
	return db[name]

def find_posts(collection, username):
	'''Find all posts by a given user.'''
	results = collection.find({"data.author":username})
	for result in results:
		print(result["data"]["title"])
	return results

def find_pop(collection, ups):
	'''Find all posts whose number of upvotes is greater than threshold.'''
	results = collection.find({"data.ups": {"$gte":ups}})
	for result in results:
		author = result["data"]["author"]
		post =  result["data"]["title"]
		print(author + ": " + post)
	return results

def find_more_pop(collection, ups, cmts):
	'''Find all posts that satisfy or exceed given number of upvotes or comments.'''
	results = collection.find({ "$or": [{"data.ups": {"gte":ups}}, {"data.num_comments":{"$gte":cmts}}]})
	for result in results:
		author = result["data"]["author"]
		post =  result["data"]["title"]
		print(author + ": " + post)
	return results


# tests
# find_posts("zeamp")
# find_pop(1000)
# find_more_pop(2000, 1000)
