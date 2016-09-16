'''
Exercise 10.7 - Missing Int:

Given an input file with four billion non-negative integers, 
provide an algorithm to generate an integer that is not contained 
in the file. Assume you have 1 GB of memory available for this task.

'''



from bitarray import bitarray


def misssingInt(numberList):
	b = bitarray(4000000000)
	a.setall(False)
	for number in numberList:
		b[number] = True

	for i in range(len(b)):
		if b[i] == False:
			return i

