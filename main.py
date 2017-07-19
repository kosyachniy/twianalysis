import csv

def read(name='base', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

word=read()[0]
print(word)