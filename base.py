import csv

def read(name='gazprom', sign=','):
	with open(name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def write(text, name='base', sign=','):
	with open(name+'.csv', 'w') as file:
		csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

word=[] #set()
k=[]
for i in read():
	for j in i[1:]:
		if j not in word:
			word.append(j) #add(j)
#
			k.append(1)
		else:
			k[word.index(j)]+=1

print(len(k))
i=0
while True:
	if i>=len(k):
		break
	if k[i]<=4: #1
		del k[i]
		del word[i]
	else:
		i+=1
print(len(k))
#
write(word)