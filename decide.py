from func import *

word=read(name=mas[ii][0]+'-base')[0]
with open('data/'+mas[ii][0]+'-weights.csv', 'r') as f:
	w=np.loadtxt(f, delimiter=',')

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