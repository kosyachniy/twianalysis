import csv

def read(name='gazprom', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

word=set()
for i in read():
	for j in i:
		if j not in word:
			word.add(j)
print(word)