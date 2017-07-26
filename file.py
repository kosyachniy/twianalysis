from func import *
import codecs

with open('data/'+mas[ii][0]+'-twits.csv', 'w') as file:
	pass

def stock(ye, mo, da):
	data=ye+'-'+mo+'-'+da
	tim=int(ye+mo+da)
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
	l=0
	for i in j['data']:
		if i[col.index('SECID')]==mas[ii][2]:
			l=round(i[col.index('CLOSE')]-i[col.index('OPEN')],2)
	return l if l else 0

if __name__=='__main__':
	k=0
	with codecs.open('data/db3.txt', 'r', 'utf8') as file:
		for i in file:
			s=json.loads(i)
			mood=stock(s['date'][6:10], s['date'][3:5], s['date'][0:2])
			try:
				write([mood]+text(s['name']), name=mas[ii][0]+'-twits', typ='a')
			except:
				print('Error in string:'+s)
			else:
				k+=1
				print(k, mood)
			time.sleep(1)