#!/usr/bin/python

x = 11
def f():
	print x

def g():
	x = 22
	print x


class c:
	x = 33
	def m(self):
		x = 44
		self.x = 55


if __name__ == '__main__':
	print x
	f()
	g()
	print x
	print c.x
	obj = c()
	print obj.x
	obj.m()
	print obj.x

	print c.x