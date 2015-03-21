from math import *

def lhs(x): 			# the left hand side of an equation
	print x
	return pow(x,2)-1.2*x-.89

def rhs(x):				# the right hand side of the equation
	return 0

def iterator(guess, step, stepAttenuation, precision, distance, direction):

	lhsResult = lhs(guess)		#calculates result
	rhsResult = rhs(guess)

	while (rhsResult > (2-precision)*lhsResult or rhsResult < precision*lhsResult): #this is our answer

		lhsResult = lhs(guess)		#calculates result
		rhsResult = rhs(guess)
		newDistance = abs(lhsResult-rhsResult)	#calculates distance from result

		if newDistance > distance:	# if we are colder
			direction = not direction

		if direction: 			# update variables	
			guess+=step
		else:
			guess-=step

		step*=stepAttenuation
		distance = newDistance
	
	print "guess:  " + str(guess)
	print "lhs: " + str(lhsResult)
	print "rhs: " + str(rhsResult)

guess = 1
step = 2
stepAttenuation = .9999
precision = .9999999
distance = 9e99
direction = True

iterator(guess, step, stepAttenuation, precision, distance, direction)
