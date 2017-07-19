import csv
import numpy as np
from parse import parse
from math import exp

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech'] in ('noun', 'adjf', 'verb'):
				y.append(j['infinitive'])
	return y

def read(name='base', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]
	return y

with open('gazprom2.csv', 'r') as f:
	data=np.loadtxt(f, delimiter=',', skiprows=1)
with open('gazprom2.csv', 'r') as f:
	y=np.loadtxt(f, delimiter=',', skiprows=1).T[0].T

x=data.T
for i in range(len(x[0])):
	x[0][i]=1
x=x.T
re=np.linalg.inv(x.T.dot(x)).dot(x.T)
w=re.dot(y)

print(w)

twit=text(input())
word=read()[0]
su=w[0]
for i in range(len(word)):
	if word[i] in twit:
		su+=w[i+1]
x=(exp(su)-exp(-su))/(exp(su)+exp(-su))
if x<0:
	print('Курс упадёт с вероятностью {}%'.format(-x*100))
elif x>0:
	print('Курс вырастет с вероятностью {}%'.format(x*100))
else:
	print('Курс не изменится')