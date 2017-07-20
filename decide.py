from func import *

word=read(name=mas[ii][0]+'-base')[0]
w=read(name=mas[ii][0]+'-weights')[0]

twit=text(input())
su=w[0]
for i in range(len(word)):
	if word[i] in twit:
		su+=w[i+1]
print('CLOSE-OPEN')
if su>0:
	print('+'+str(su))
else:
	print(su)