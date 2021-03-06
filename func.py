import requests, json, csv, re, time
from parse import parse
import numpy as np

mas=[['gazprom','газпром','GAZP'],['sberbank','сбербанк','SBRF'],['aeroflot','аэрофлот','AFLT']]
ii=0 #

get=lambda src: requests.get(src).text

def delete(name):
	with open('data/'+mas[ii][0]+'-'+name+'.csv', 'w') as file:
		pass

def write(text, name, typ='a', sign=','):
	if len(text):
		with open('data/'+mas[ii][0]+'-'+name+'.csv', typ) as file:
			csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

def read(name, sign=','):
	with open('data/'+mas[ii][0]+'-'+name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def numread(name, nom=0):
	with open('data/'+mas[ii][0]+'-'+name+'.csv', 'r') as f:
		return np.loadtxt(f, delimiter=',', skiprows=nom)

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech'] in ('noun', 'adjf', 'verb'):
				y.append(j['infinitive'])
	return y