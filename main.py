import csv
from numpy import *

def read(name='base', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def write(text, name='gazprom2', sign=','):
	with open(name+'.csv', 'a') as file:
		csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

word=read(name='base')[0]
twit=read(name='gazprom')
twits=[]
for i in range(len(twit)):
	twits.append([twit[i][0]])
	for j in word:
		twits[i].append(1) if j in twit[i] else twits[i].append(0)
for i in twits:
	write(i)