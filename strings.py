with open('data/aeroflot-twits.csv', 'r')  as f:
	with open('data/db.csv', 'a') as q:
		for i in f:
			if len(i)>1:
				print(i, file=q, end='')