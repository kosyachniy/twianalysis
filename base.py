import csv

def read(name='gazprom', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def write(text, name='base', sign=','):
	with open(name+'.csv', 'w') as file:
		csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

word=set()
for i in read():
	for j in i[1:]:
		if j not in word:
			word.add(j)
write(word)