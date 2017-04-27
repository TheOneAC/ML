#!/usr/bin/python


'''
display class tree
'''
def classtree(cls, indent):

	for supcls in cls.__bases__:
		classtree(supcls, indent+3)
	print ('.' * indent + cls.__name__)
	

def instancetree(inst):
	print ('tree of %s' % inst)
	classtree(inst.__class__, 3)



def selftest():
	class A(object): pass
	class B(A):pass
	class C(A):pass
	class D(B, C): pass
	class E():pass
	class F(D, E):pass
	instancetree(B())
	instancetree(F())


if __name__ == '__main__':
	selftest()
