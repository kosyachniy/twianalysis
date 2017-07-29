m=[]
with open('data/gazprom-twits.csv', 'r') as file:
	for i in file:
		m.append(i)

j=1
while j<len(m)-1:
	if m[j][0:2]=='0,':
		j-=1
		del m[j]
		del m[j]
		del m[j]
	else:
		j+=1

with open('data/gazprom-twits.csv', 'w') as file:
	for i in m:
		print(i, file=file, end='')