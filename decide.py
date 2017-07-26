from func import *

def decide(cont):
	word=read(name='base')[0]
	w=numread('weights')

	k=0
	su=w[0]
	for i in range(len(word)):
		if word[i] in text(cont):
			k+=1
			su+=w[i+1]

	su=round(su, 2) if k else 0
	return ('+'+str(su) if su>0 else str(su)) if su else 'По этим данным невозможно предсказать курс!'

if __name__=='__main__':
	a=decide(input())
	print('==========')
	if a[0] in ('+','-'):
		print('CLOSE-OPEN')
	print(a,'\n==========')