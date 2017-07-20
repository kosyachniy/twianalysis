from func import *
import tweepy

with open(mas[ii][0]+'.csv', 'w') as file:
	pass

#Авторизация
def auth(user='ritapoloz'):
	with open('set.txt', 'r') as file:
		s=json.loads(file.read())
		consumer_key, consumer_secret=s['key']['main']
		access_key, access_secret=s['key'][user]

	aut=tweepy.OAuthHandler(consumer_key, consumer_secret)
	aut.set_access_token(access_key, access_secret)
	return tweepy.API(aut)

def stock(ti):
	data='{}-{}-{}'.format(ti.year,ti.month,ti.day)
	da=str(ti.day) if ti.day>=10 else '0'+str(ti.day)
	mo=str(ti.month) if ti.month>=10 else '0'+str(ti.month)
	tim=int(str(ti.year)+mo+da)
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
	api=auth()
	k=0
	#Создаются лишние строки
	for i in tweepy.Cursor(api.user_timeline, id=mas[ii][0]).items():
		if not i.is_quote_status and not i.in_reply_to_user_id and not i.in_reply_to_status_id:
			mood=stock(i.created_at)
			try:
				write([mood]+text(re.sub(r'https://t.co/\w+$', '', re.sub(r'https://t.co/\w+ ', '', i.text))), name=mas[ii][0], typ='a')
			except:
				print('Error in tweet №{}'.format(i.id))
			else:
				k+=1
				print(k, mood)
			time.sleep(1)