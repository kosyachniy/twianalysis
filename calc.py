from func import *

with open('data/'+mas[ii][0]+'-table.csv', 'r') as f:
	data=np.loadtxt(f, delimiter=',', skiprows=1)
with open('data/'+mas[ii][0]+'-table.csv', 'r') as f:
	y=np.loadtxt(f, delimiter=',', skiprows=1).T[0].T

x=data.T
for i in range(len(x[0])):
	x[0][i]=1
x=x.T
re=np.linalg.inv(x.T.dot(x)).dot(x.T)
w=re.dot(y)

np.savetxt('data/'+mas[ii][0]+'-weights.csv', w, delimiter=',')
print(w)