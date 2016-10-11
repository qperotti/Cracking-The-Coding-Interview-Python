'''
Exercise 8.5 - Recursive Multiply:

Write a recursive function to multiply two positive integers without 
using the * operator or / operator. You can use addition, substraction, 
and bit shifting, but you should minimize the number of those operations.
'''

def recursiveMultiply(a,b):

	def multiply(a,b):

		if a == 1:
			return b
		return b + multiply(a-1,b)


	smaller = a if a < b else b
	bigger = b if a < b else a

	
	half = multiply(smaller//2,bigger)
	
	if smaller%2 == 0:
		return half + half
	else:
		return half + half + bigger




if __name__ == '__main__':

	print(recursiveMultiply(17,23))