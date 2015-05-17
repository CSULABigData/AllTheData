# '''
# Created on Apr 22, 2015
# 
# @author: Alex
# '''
import oauth2 as oauth
import json
import pymongo
import datetime
# 

#Variables that contains the user credentials to access Twitter API 

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
 
client = pymongo.MongoClient()
db = client.tweetcounts
storyName = "Linux"
trackWord = ["Linux", "Ubuntu"]


 #This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
 
	def on_data(self, data):
		year = datetime.datetime.now().year
		month = datetime.datetime.now().month
		day = datetime.datetime.now().day
		hour = datetime.datetime.now().hour
		if(db.counts.count({'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour}) > 0):
			count = db.counts.find_one({'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour}).get('count')
			db.counts.update({'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour},
				{'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour, 'count':count + 1})
		else:
			db.counts.insert({'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour, 'count':1})
		print db.counts.find_one({'name':trackWord, 'year': year, 'month': month, 'day': day, 'hour': hour}).get('count')
		return True
 
	def on_error(self, status):
		print status	
 
if __name__ == '__main__':
 
	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(track=trackWord)








