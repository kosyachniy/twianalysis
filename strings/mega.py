m=[]
with open('data/gazprom-twits.csv', 'r') as file:
	for i in file:
		m.append(i)

j=0
while j<len(m):
	if (('-'==m[j][0]) and '.' not in m[j][0:3]) or (('-'!=m[j][0]) and ('.' not in m[j][0:2])):
		del m[j]
	else:
		j+=1

with open('data/gazprom-twits.csv', 'w') as file:
	for i in m:
		print(i, file=file, end='')