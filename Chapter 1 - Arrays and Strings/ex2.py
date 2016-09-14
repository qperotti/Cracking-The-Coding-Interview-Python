'''
Exercise 1.2 - Check Permutation:

Given two strings, write a method to decide if one is a permutation of the other.

O(n) solution
'''


def stringToDict(s):
	character_dict = dict()
	for character in s:
		if character not in character_dict:
			character_dict[character] = 1
		else:
			character_dict[character] += 1
	return character_dict


def checkPermutation(s1, s2):

	if len(s1) != len(s2):
		return False

	s1_dict = stringToDict(s1)
	s2_dict = stringToDict(s2)

	if len(s1_dict) != len(s2_dict):
		return False	

	for character in s1_dict:
		if not (character in s2_dict and s1_dict[character] == s2_dict[character]):
			return False
		

	return True


if __name__ == "__main__":

	# True
	print(checkPermutation('hello world','world hello'))
	print(checkPermutation('dogandcat','catanddog'))

	# False
	print(checkPermutation('hello world','world hell'))
	print(checkPermutation('dogandcat','doganddog'))