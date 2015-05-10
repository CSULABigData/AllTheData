# '''
# Created on Apr 22, 2015
# 
# @author: Alex
# '''
# import oauth2 as oauth
# import json
# 
# 
# keyword = raw_input("Enter a keyword:")
# # Set the API endpoint 
# 
# token = oauth.Token(key="", secret="")
# consumer = oauth.Consumer(key="", secret="")
# searchURL = 'https://api.twitter.com/1.1/search/tweets.json?q=%23' + str(keyword)
# client = oauth.Client(consumer, token)
# 
# response, data = client.request(searchURL)
# 
# tweets = json.loads(data)
# print(json.dumps(tweets, sort_keys=True))

#Variables that contains the user credentials to access Twitter API 

#Import the necessary methods from tweepy library
# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream

# access_token = "ENTER YOUR ACCESS TOKEN"
# access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
# consumer_key = "ENTER YOUR API KEY"
# consumer_secret = "ENTER YOUR API SECRET"
# 
# 
# #This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):
# 
#     def on_data(self, data):
#         print data
#         return True
# 
#     def on_error(self, status):
#         print status
# 
# 
# if __name__ == '__main__':
# 
#     #This handles Twitter authetification and the connection to Twitter Streaming API
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)
# 
#     #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#     stream.filter(track=['python', 'javascript', 'ruby'])

import sys
print sys.path







