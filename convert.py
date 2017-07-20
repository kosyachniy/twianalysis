from func import *

with open('gazprom2.csv', 'w') as file:
	pass

word=read(name='base')[0]
twit=read(name='gazprom')
twits=[]
write(['!']+['"'+i+'"' for i in word], name='gazprom2')
for i in range(len(twit)):
	twits.append([twit[i][0]])
	for j in word:
		twits[i].append(1) if j in twit[i] else twits[i].append(0)
for i in twits:
	write(i, name='gazprom2')