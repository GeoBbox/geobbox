# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:00:49 2015

@author: girloffroad

This code will populate a mongodb from multiple json files located across
 one or several folders. For each folder, this code creates a collection of the
 same name and inserts documents into the collection as the code reads each line
 of each json file in the folder.

For example, let's say you have a folder called dataset, and in there
are folders such as day1 day2 day3. In each folder is a set of json files with
1 or several objects such as tweets. This code will create collections called day1 day2
day 3, and fill each collection with documents for each individual json object or tweet
contained in each of the json files located in the folder associated with that collection.

Code is based on combining:
multiple folders full of json files:
http://syntx.io/an-import-utility-to-import-json-docs-into-mongodb-in-python/
and  for reading several tweets per json file:
https://github.com/pablobarbera/pytwools/blob/master/tweets-to-mongo.py#L35

In the same folder as this code, create a folder called dataset and place the folders
with json files in there.


To run this code first make sure mongod is running in a terminal
and you use the database you want to populate.

Then run this code.

Notes: This code is written for Python3 by modifying print statements to print()

"""

from pymongo import MongoClient
import os
from os.path import join
from genericpath import isfile
import json
import traceback
import random
import datetime

connection_string = 'mongodb://127.0.0.1:27017/geobbox1' #enter the db name instead of geobbox1
print ('connecting to mongodb at:' + connection_string)

client = MongoClient(connection_string)
db = client.get_default_database()

print ('beginning to read files')


# need this to import object keys for mongo
def add_fields(tweet):
    # index field
    tweet['_id'] = tweet['id_str']
    # timestamp
    tweet['timestamp'] = datetime.datetime.strptime(
        tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'
    )
    # random number
    tweet['random_number'] = random.random()
    return(tweet)


try:
    path = 'dataset' # enter the location and name of the folder containing your folders with json
    folders = 0
    jsons = 0
    objects = 0
    collections = [collections for collections in os.listdir(path) if not isfile(join(path, collections))]
    for collection in collections:
        folders = folders + 1
        print ('processing collection:' + collection)
        mongo_collection = db[collection]
        files = [files for files in os.listdir(join(path, collection))]
        for file in files:
            jsons = jsons + 1  # count number of files processed
            filepath = path + '/' + collection + '/' + file
            print ('processing file :' + filepath)
            filehandle = open(filepath, 'r')
            for line in filehandle:
                try:
                    # reading tweet
                    tweet = json.loads(line)
                except:
                    continue
                try:
                    # adding fields
                    tweet = add_fields(tweet)
                    # adding to mongo
                    mongo_collection.insert(tweet)
                    objects = objects + 1
                except:
                    continue
        filehandle.close()
    folders = folders + 1
    print ('Done! Processed ' + str(jsons) +
        ' json files. Added  ' + str(folders) +
        ' collections to your database. Inserted a total of ' +
        str(objects) + ' documents.')
except Exception as e:
    traceback.print_exc()
