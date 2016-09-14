'''
Exercise 1.4 - Palindrome Permutation:

Given a string, write a function to check if it is a permutation of a palindrome.
The palindrome does not need to be limited to just dictionary words.
'''


def checkPalindrome(s):

	# number of odd counts
	count = 0

	char_dict = dict()
	for character in s:
		if character != ' ':
			if character not in char_dict:
				char_dict[character] = 1
				count += 1
			else:
				char_dict[character] += 1
				if char_dict[character] % 2 == 0:
					count -= 1
				else:
					count += 1
	return count


def palindromePermutation(s):

	count = checkPalindrome(s)
	return count <= 1


if __name__ == "__main__":

	# True
	print(palindromePermutation('atco cta'))
	print(palindromePermutation('aaabb cc'))

	# False
	print(palindromePermutation('hello world'))
	print(palindromePermutation('aaa bbb cc'))