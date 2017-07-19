import tweepy, csv
from json import *
from parse import parse

#Авторизация
def auth(user='ritapoloz'):
	with open('set.txt', 'r') as file:
		s=loads(file.read())
		consumer_key, consumer_secret=s['key']['main']
		access_key, access_secret=s['key'][user]

	aut=tweepy.OAuthHandler(consumer_key, consumer_secret)
	aut.set_access_token(access_key, access_secret)
	return tweepy.API(aut)

def write(text, name='gazprom', sign=','):
	with open(name+'.csv', 'a') as file:
		csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech']!='sign':
				y.append(j['infinitive'])
	return y

api=auth()
for i in api.user_timeline('gazprom'):
	#Не все
	write(text(i.text))