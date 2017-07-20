from func import *

with open('data/'+mas[ii][0]+'-table.csv', 'w') as file:
	pass

word=read(name=mas[ii][0]+'-base')[0]
twit=read(name=mas[ii][0]+'-twits')
twits=[]
write(['!']+['"'+i+'"' for i in word], name=mas[ii][0]+'-table')

#
i=0
while i<len(twit):
	if twit[i]:
		i+=1
	else:
		del twit[i]
#

for i in range(len(twit)):
	twits.append([twit[i][0]])
	for j in word:
		twits[i].append(1) if j in twit[i] else twits[i].append(0)

for i in twits:
	write(i, name=mas[ii][0]+'-table')