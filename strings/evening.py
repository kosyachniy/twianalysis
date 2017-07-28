import json

m=[]

with open('data/gazprom-news.txt') as f:
	for i in f:
		time=json.loads(i)['date']
		day=int(time[0:2])
		month=int(time[3:5])
		year=int(time[6:10])
		hour=int(time[12:14])
		minute=int(time[15:17])

		m.append([day, month, year, hour, minute, json.loads(i)['name']])

def pred(i):
	for j in m[:i][::-1]:
		if j[0]!=m[i][0]:
			return j[0], j[1], j[2]
	return [False]

def sled(i):
	for j in m[i:]:
		if j[0]!=m[i][0]:
			return j[0], j[1], j[2]
	return [False]

for i in range(len(m)):
	if m[i][3]*100+m[i][4]>1830:
		print('OPEN-CLOSE', pred(i), (m[i][0], m[i][1], m[i][2]))
	elif hour*100+minute<1000:
		print('OPEN-CLOSE', (m[i][0], m[i][1], m[i][2]), sled(i))
	else:
		print('CLOSE-OPEN', (m[i][0], m[i][1], m[i][2]))