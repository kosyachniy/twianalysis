from func2 import *

def decide(cont):
	word=read(name=mas[ii][0]+'-base')[0]
	with open('data/'+mas[ii][0]+'-weights.csv', 'r') as f:
		w=np.loadtxt(f, delimiter=',')

	twit=text(cont)
	su=w[0]
	k=0
	for i in range(len(word)):
		if word[i] in twit:
			k+=1
			su+=w[i+1]
	return su if k else 0