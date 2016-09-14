'''
Exercise 1.5 - One way:

There are three types of edits can be performed on strings: 
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

def checkInsertRemove(s1, s2):
	indexS1 = 0
	indexS2 = 0
	foundDiff = False

	while indexS2 < len(s2):
		if s1[indexS1] != s2[indexS2]:
			if foundDiff:
				return False
			foundDiff = True
		else:
			indexS2 += 1
		indexS1 += 1
	return True


def checkReplace(s1,s2):
	foundDiff = False
	for char1,char2 in zip(s1,s2):
		if char1 != char2:
			if foundDiff:
				return False
			foundDiff = True
	return True

def oneWay(s1,s2):
	
	if s1 == s2:
		return True

	if abs(len(s1)-len(s2)) > 1:
		return False

	if len(s1) == len(s2):
		return checkReplace(s1,s2)
	elif len(s1) > len(s2):
		return checkInsertRemove(s1,s2)
	else:
		return checkInsertRemove(s2,s1)

if __name__ == "__main__":

	# True
	print(oneWay('pale','ple'))
	print(oneWay('pales','pale'))
	print(oneWay('pale','bale'))

	# False
	print(oneWay('pale','bae'))