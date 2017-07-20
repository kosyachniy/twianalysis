from func import *

with open(mas[ii][0]+'2.csv', 'w') as file:
	pass

word=read(name='base')[0]
twit=read(name=mas[ii][0])
twits=[]
write(['!']+['"'+i+'"' for i in word], name=mas[ii][0]+'2')

i=0
while i<len(twit):
	if twit[i]:
		i+=1
	else:
		del twit[i]

for i in range(len(twit)):
	twits.append([twit[i][0]])
	for j in word:
		twits[i].append(1) if j in twit[i] else twits[i].append(0)

for i in twits:
	write(i, name=mas[ii][0]+'2')