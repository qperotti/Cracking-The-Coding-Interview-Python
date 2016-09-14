'''
Exercise 1.1 - Is Unique:

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def isUnique_DS(s):

	# Create a set to keep track of viewed characters
	characters_set = set()

	for character in s:
		if character in characters_set:
			return False
		else:
			characters_set.add(character)
	return True


def isUnique_Pythonic(s):
	return len(s) == len(set(s))


def isUnique_NO_DS(s):
	aux = sorted(s)

	for i in range(1,len(s)):
		if aux[i] == aux[i-1]:
			return False
	return True


if __name__ == "__main__":

	# True
	print(isUnique_DS('asdfghjkl qwertyuiop'))
	print(isUnique_Pythonic('asdfghjkl qwertyuiop'))
	print(isUnique_NO_DS('asdfghjkl qwertyuiop'))

	# False
	print(isUnique_DS('asdfghjkl qwertyuiop a'))
	print(isUnique_Pythonic('asdfghjkl qwertyuiop a '))
	print(isUnique_NO_DS('asdfghjkl qwertyuiop a'))