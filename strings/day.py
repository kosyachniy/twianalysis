import csv

def read(name='data/gazprom-twits', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def write(text, name='data/db', sign=','):
	with open(name+'.csv', 'a') as file:
		csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

if __name__=='__main__':
	cont=read()
	i=0
	while i<len(cont)-1:
		if cont[i][0]==cont[i+1][0]:
			cont[i].extend(cont[i+1][1:])
			del cont[i+1]
		else:
			i+=1
	for i in cont:
		write(i)