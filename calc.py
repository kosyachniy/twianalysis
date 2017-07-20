from func import *
import numpy as np
from math import exp

with open(mas[ii][0]+'-table.csv', 'r') as f:
	data=np.loadtxt(f, delimiter=',', skiprows=1)
with open(mas[ii][0]+'-table.csv', 'r') as f:
	y=np.loadtxt(f, delimiter=',', skiprows=1).T[0].T

x=data.T
for i in range(len(x[0])):
	x[0][i]=1
x=x.T
re=np.linalg.inv(x.T.dot(x)).dot(x.T)
w=re.dot(y)

write(w, name=mas[ii][0]+'-weights')
print(w)