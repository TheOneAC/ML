#!/usr/bin/python


class Super():
	def method(self):
		print 'in super method'
	def delegate(self):
		self.action()
		#assert False, 'action must be defined'
		#print 'spam'

class Inheritor(Super):
	pass


class Replace(Super):
	def method(self):
		print 'in replace method'


class Extender(Super):
	def method(self):
		print 'starting extender method'
		Super.method(self)
		print 'end extender method'

class Provider(Super):
	def action(self):
		print 'in provider action'


if __name__ == '__main__':
	for kclass in (Replace, Inheritor, Extender):
		print '\n' + kclass.__name__ + '...'
		kclass().method()
	print '\nprovider.....'
	x = Provider()
	x.delegate()
	