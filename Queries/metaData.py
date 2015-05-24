import pymongo
import sys

client = pymongo.MongoClient()
db = client.tweetcounts

if __name__ == '__main__':

	tmpList = db.counts.find()
	
	sum = 0
	count = 0
	
	for i in tmpList:
		sum += i.get('count')
		count = count + 1
		
	print sum
	print sum * 7 / count

