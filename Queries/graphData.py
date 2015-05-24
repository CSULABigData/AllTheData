import pymongo
import sys

client = pymongo.MongoClient()
db = client.tweetcounts

if __name__ == '__main__':

	tmpList = db.counts.find({'name':sys.argv[1]})

	for i in tmpList:
		if sys.argv[2] == '1':
			if 10 < i.get('hour') < 15:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(i.get('count'))
			else:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(0)

		if sys.argv[2] == '2':
			if not 3 < i.get('hour') < 21:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(i.get('count'))
			else:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(0)
				
		if sys.argv[2] == '3':
			if True:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(i.get('count'))
			else:
				print str(float(i.get('day')) + float(i.get('hour')) / 24.0) + '\t' + str(0)
