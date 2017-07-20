from func import *

word=[] #set()
k=[]
for i in read(name='gazprom'):
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
write(word, name='base', typ='w')