'''
Exercise 1.9 - String Rotation:

Assume you have a method isSubstring which checks if one 
word is a substring of another. Given two strings, s1 and 
s2 write code to check if s2 is a rotation of s1 using only 
one call to isSubstring.
'''


def isSubstring(s1, s2):
    return s1.find(s2) != -1


def stringRotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s1, s2)
    return False


if __name__ == "__main__":

	# True
	print(stringRotation('waterbottle', 'erbottlewat'))
	print(stringRotation('helloworld', 'worldhello'))

	# False
	print(stringRotation('catdog', 'cotdag'))
	print(stringRotation('string', 'lol'))

