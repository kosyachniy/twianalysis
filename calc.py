from func import *

x=numread('table', 1).T
for i in range(len(x[0])):
	x[0][i]=1
x=x.T

y=numread('table', 1).T[0].T

re=np.linalg.inv(x.T.dot(x)).dot(x.T)
w=re.dot(y)

np.savetxt('data/'+mas[ii][0]+'-weights.csv', w, delimiter=',')
print(w)