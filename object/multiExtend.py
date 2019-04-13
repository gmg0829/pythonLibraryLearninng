class Father(object):

	def __init__(self, name):
		self._name = name

	def gamble(self):
		print('%s在打麻将.' % self._name)

	def eat(self):
		print('%s在大吃大喝.' % self._name)


class Monk(object):

	def __init__(self, name):
		self._name = name

	def eat(self):
		print('%s在吃斋.' % self._name)

	def chant(self):
		print('%s在念经.' % self._name)


class Musician(object):

	def __init__(self, name):
		self._name = name

	def eat(self):
		print('%s在细嚼慢咽.' % self._name)

	def play_piano(self):
		print('%s在弹钢琴.' % self._name)


# 试一试下面的代码看看有什么区别
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

	def __init__(self, name):
		Father.__init__(self, name)
		Monk.__init__(self, name)
		Musician.__init__(self, name)


son = Son('王大锤')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()