import tensorflow as tf
from func import *

#Данные
with open('data/'+mas[ii][0]+'-table.csv', 'r') as f:
	data=np.loadtxt(f, delimiter=',', skiprows=1)
with open('data/'+mas[ii][0]+'-table.csv', 'r') as f:
	yyy=np.loadtxt(f, delimiter=',', skiprows=1).T[0].T

xx=data.T
for i in range(len(xx[0])):
	xx[0][i]=1
xx=xx.T

qw=[]
for i in yyy:
	qw.append([float(i)])
yy=np.array(qw)

#Объявляем входное значение x, вес w, какое значение должны получить y
x = tf.placeholder(tf.float32, shape=(len(xx[0]),))
y = tf.placeholder(tf.float32, shape=(1,))
w = tf.Variable(tf.zeros([1, len(xx[0])]))
#b = tf.Variable(tf.zeros([1]))

#Получаем выходное значение
#y2 = tf.add(tf.multiply(x, w), b)
y2=tf.multiply(x, w)

#Рассчитываем ошибку выходных данных
loss = tf.reduce_mean(tf.square(y-y2))
optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

#Запуск обучения
with tf.Session() as session:
	tf.global_variables_initializer().run()
	for j in range(100):
		for i in range(len(xx)):
			feed_dict={x: xx[i:(i+1)][0], y: yy[i:(i+1)][0]}
			_, l = session.run([optimizer, loss], feed_dict=feed_dict)
			print("ошибка: %f" % (l, ))

	iii=session.run(w)[0]
	np.savetxt('data/'+mas[ii][0]+'-weights.csv', iii, delimiter=',')
	print(iii)