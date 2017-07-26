import requests, json, csv, re, time
from parse import parse
import numpy as np

mas=[['gazprom','газпром','GAZP'],['sberbank','сбербанк','SBRF'],['aeroflot','аэрофлот','AFLT']]
ii=0 #

def get(src):
	return requests.get(src).text

def write(text, name=mas[ii][0], typ='a', sign=','):
	if len(text):
		with open('data/'+name+'.csv', typ) as file:
			csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

def read(name=mas[ii][0], sign=','):
	with open('data/'+name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech'] in ('noun', 'adjf', 'verb'):
				y.append(j['infinitive'])
	return y