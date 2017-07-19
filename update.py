#Создание файлов с текстами для обучения нейронной сети

import csv, sys, socket
from parse import parse
if sys.version_info[0]>=3:
	from urllib.request import urlretrieve, urlopen
else:
	from urllib import urlretrieve, urlopen

adr='http://zodzu.com/'

def internet():
	try:
		socket.gethostbyaddr('www.yandex.ru')
	except socket.gaierror:
		return False
	return True

def download():
	urlretrieve(adr+'input.txt','db/input.txt')
	urlretrieve(adr+'output.txt','db/output.txt')

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech']!='sign':
				y.append(j['infinitive'])
	return y

if internet() and urlopen(adr+'input.txt') and urlopen(adr+'output.txt'):
	download()
m=['input','output']
for i in m:
	out=open('db/'+i+'.txt','r')
	with open('db/'+i+'.csv', 'w') as file:
		w=csv.writer(file,quotechar=' ',quoting=csv.QUOTE_MINIMAL)
		for j in out:
			w.writerow(text(j.strip()))
	out.close()