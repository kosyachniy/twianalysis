import requests, json

def get(src):
	return requests.get(src).text

if __name__=='__main__':
	data='2013-12-20'
	j=json.loads(get('http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqne/securities.json?date='+data))['history']
	col=j['columns']
	for i in j['data']:
		if i[col.index('SECID')]=='GAZP':
			print(round(i[col.index('CLOSE')]-i[col.index('OPEN')],2))