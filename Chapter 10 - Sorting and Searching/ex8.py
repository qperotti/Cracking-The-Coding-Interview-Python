'''
Exercise 10.8 - Find Duplicates:

You have an array with all the numbers from 1 to N, where N 
is at most 32,000. The array may have duplicate entries and 
you do not know what N is. With only 4 kb of memory available, 
how would you print all duplicates elements in the array.

'''

from bitarray import bitarray


def findDuplicates(numberList):
	b = bitarray(32000)
	a.setall(False)
	for number in numberList:
		if b[number] == True:
			print(number)
		b[number] = True
