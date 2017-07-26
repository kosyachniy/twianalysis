from func import *
from decide import decide

mess={'хай', 'привет', 'здарова', 'здаров', 'ghbdtn', '[fq', 'hay', 'hello', 'хело', 'хелло', 'хеллоу', 'хелоу', 'хей', 'здрасте', 'здрасть', 'здраст', 'эй', 'приветики', 'пивет', 'здравствуйте', 'здравствуй', 'здраствуй', 'здраствуйте', 'добро пожаловать', 'рад познакомиться', 'будем знакомы', 'хой'}

def hello(cont):
	if any(i in cont for i in mess):
		return True
	return False

while True:
	for id in dial():
		for i in read(id):
			if hello(i):
				send(id, 'Привет! Это бот с использованием нейронных сетей для предсказания курса бирж. На данный момент мы работаем исключительно с биржой Газпрома. Напиши новость и мы попробуем предсказать изменение курса!')
			else:
				cont=round(decide(i)*100000000, 2) #
				send(id, '+'+str(cont) if cont>0 else cont)
	time.sleep(5)