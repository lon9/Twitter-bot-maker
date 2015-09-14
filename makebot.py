import argparse
import os.path
import tweepy
import webbrowser
import sys
import shutil

def getAuth():
	consumerKey = input('Consumer key:')
	consumerSecret = input('Consumer Secret:')
	consumerkey = consumerKey.strip()
	consumerSecret = consumerSecret.strip()
	if not consumerKey:
		print('Please input consumer key.')
		sys.exit()
	if not consumerSecret:
		print('Please input consumer secret.')
		sys.exit()
	
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	url = auth.get_authorization_url()
	webbrowser.open(url)
	validCode = input('Validation code:')
	validCode.strip()
	if not validCode:
		print('Please input validation code in your browser.')
		sys.exit()
	auth.get_access_token(validCode)
	return auth

def createCode(filename, auth):
	f = open(filename, "r")
	tweetsList = []
	for line in f:
		tweetsList.append("'"+line[:-1]+"'")
	tweets = ",".join(tweetsList)
	f.close()

	code = '''
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
	'''.format(consumerKey=auth.consumer_key.decode('utf-8'), consumerSecret=auth.consumer_secret.decode('utf-8'), 
			accessToken=auth.access_token, accessTokenSecret=auth.access_token_secret, tweets=tweets)
	return code

def createFiles(code, dirpath):
	templates = os.path.abspath('templates')
	shutil.copytree(templates, dirpath+'/bot')
	f = open(dirpath+'/bot/bot.py', "w")
	f.write(code)
	f.close()
	
	
def main(filename, dirpath):
	auth = getAuth()
	code = createCode(filename, auth)
	createFiles(code, dirpath)
	print('Twitter bot was generated in %s/bot' %dirpath)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Making twitter bot.')
	parser.add_argument('file', metavar='Tweets file name', type=str, nargs=1)
	parser.add_argument('path', metavar='Directory path', type=str, nargs=1)
	args = parser.parse_args()
	filename = args.file[0]
	dirpath = args.path[0]
	if os.path.isfile(filename) and os.path.isdir(dirpath):
		main(filename, dirpath)
	else:
		print('File or directory is not existed')

