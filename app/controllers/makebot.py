# -*- coding:utf-8 -*-
import zipfile
import os.path
import os
import shutil

class MakeBot:
	def __init__(self, auth):
		self.auth=auth
		self.dirname=''

	def makeZip(self, tweetFilePath):
		# tweetFilePath like .../tmp/RANDOM/tweetFile abspath
		f = open(tweetFilePath, "r")
		tweetsList = []
		for line in f:
			tweetsList.append("'"+line[:-1]+"'")
		tweets = ",".join(tweetsList)
		f.close()
		code = """
import tweepy
import random

CONSUMER_KEY='{consumerKey}'
CONSUMER_SECRET='{consumerSecret}'
ACCESS_TOKEN='{accessToken}'
ACCESS_TOKEN_SECRET='{accessTokenSecret}'

tweets = [{tweets}]
	
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def tweet():
	rand = random.randint(0,len(tweets)-1)
	tweet = tweets[rand]
	api.update_status(status=tweet)
		""".format(consumerKey=self.auth.consumer_key.decode('utf-8'), consumerSecret=self.auth.consumer_secret.decode('utf-8'), accessToken=self.auth.access_token, accessTokenSecret=self.auth.access_token_secret, tweets=tweets)

		dirname = os.path.dirname(tweetFilePath)
		self.dirname=dirname
		# dirname like .../tmp/RANDOM
		shutil.copytree('templates', dirname+'/bot')
		f = open(dirname+'/bot/bot.py', "w")
		f.write(code)
		f.close()
		zip = zipfile.ZipFile(dirname+"/"+os.path.basename(dirname)+".zip", "w", zipfile.ZIP_DEFLATED)
		files = os.listdir(dirname+'/bot')
		for f in files:
			zip.write(dirname+'/bot/'+f, 'bot/'+f)
		zip.close()

	def deleteFiles(self):
		os.rmdir(self.dirname)

	def getDirPath(self):
		return self.dirname
