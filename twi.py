import tweepy, csv, re, time
from json import *
from parse import parse

with open('gazprom.csv', 'w') as file:
	pass

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
			if j['speech'] in ('noun', 'adjf', 'verb'):
				y.append(j['infinitive'])
	return y

if __name__=='__main__':
	api=auth()
	k=0
	for i in tweepy.Cursor(api.user_timeline, id='gazprom').items():
	#for i in api.user_timeline('gazprom'):
		#mood=int(input(i.text))
		write([0]+text(re.sub(r'https://t.co/\w+$', '', re.sub(r'https://t.co/\w+ ', '', i.text))))
		k+=1
		time.sleep(1)
		if k>=500:
			break