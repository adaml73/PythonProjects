def recurPower(base, exp):
	'''
	base: int or float
	exp: int >= 0
	
	returns: int or float, base^exp
	'''
	
exp = 5
base = 5

if exp <= 0:
	print 1

print base * recurPower(base, exp - 1)
	