from func import *
import codecs

delete('twits')

def stock(da, mo, ye):
	data=str(ye)+'-'+str(mo)+'-'+str(da)
	tim=(ye*100+mo)*100+da

	if tim>=20140609:
		border='tqbr'
	elif tim>=20131226:
		border='tqbs'
	elif tim>=20130325:
		border='tqne'
	elif tim>=20060123:
		border='eqne'

	j=json.loads(get('http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/'+border+'/securities.json?date='+data))['history']
	col=j['columns']
	for i in j['data']:
		if i[col.index('SECID')]==mas[ii][2]:
			return i[col.index('CLOSE')], i[col.index('OPEN')]
	return 0, 0

m=[]
with codecs.open('data/'+mas[ii][0]+'-news.txt', 'r', 'utf8') as file:
	for i in file:
		date=json.loads(i)['date']
		day=int(date[0:2])
		month=int(date[3:5])
		year=int(date[6:10])
		hour=int(date[12:14])
		minute=int(date[15:17])

		if (year*100+month)*100+day<20060123: break
		m.append([day, month, year, hour, minute, json.loads(i)['name']])

print(len(m))

def pred(i):
	for j in m[:i][::-1]:
		if j[0]!=m[i][0]:
			return j[0], j[1], j[2]
	return ()

def sled(i):
	for j in m[i:]:
		if j[0]!=m[i][0]:
			return j[0], j[1], j[2]
	return ()

k=0
n=[]
for i in range(len(m)):
	try:
		if m[i][3]*100+m[i][4]>1830:
			q=pred(i)
			if len(q):
				mood=stock(*q)[1]-stock(m[i][0], m[i][1], m[i][2])[0]
			else:
				continue
		elif hour*100+minute<1000:
			q=sled(i)
			if len(q):
				mood=stock(m[i][0], m[i][1], m[i][2])[1]-stock(*q)[0]
			else:
				continue
		else:
			cl, op=stock(m[i][0], m[i][1], m[i][2])
			mood=cl-op
	except:
		print('Error in string:', m[i])
	else:
		k+=1
		print(k, mood)
	time.sleep(1)

	if len(n) and n[len(n)-1][0]==m[i][0]:
		n[len(n)-1].extend(text(m[i][5]))
	else:
		n.append([m[i][0], mood]+text(m[i][5]))

print(len(n))

for i in n:
	write(i[1:], name='twits', typ='a')