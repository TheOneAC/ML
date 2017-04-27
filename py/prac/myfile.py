#!/usr/bin/python


title = "the meaning of life"


class person(object):
	def __init__(self, name, job=None, pay =0):
		self.name = name
		self.job = job
		self.pay = pay
	def last_name(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

	def __str__(self):
		return '[person: %s, %s]' %(self.name, self.pay)




class manager(person):
	def __init__(self, name, pay):
		person.__init__(self, name,'mgr', pay)
	def giveRaise(slef, percent, bonus = .10):
		person.giveRaise(self, percent + bonus)



if __name__ == '__main__':
	bob = person('bob smith')
	sue = person('sue jones', job ='dev', pay =100000)
	print bob.name, bob.pay
	print sue.name, sue.pay
	print sue.last_name(), bob.last_name()
	sue.giveRaise(.10)
	print sue.pay
	print sue
	print bob.__class__.__name__
	for key in bob.__dict__:
		print (key , '=>', bob.__dict__[key])


	import shelve
	db = shelve.open('persondb')
	for obj in (bob, sue):
		db[obj.name] = obj
	db.close()

	db = shelve.open('persondb')
	for key in db:
		print key, '=>', db[key]