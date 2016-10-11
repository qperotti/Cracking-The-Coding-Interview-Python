'''
Exercise 8.7 - Permutations without Dups:

Write a method to compute all permutations of a string of unique characters.
'''

from collections import deque



def allPermutations(S):

	permutations = deque()
	permutations.append([])

	for char in S:

		total = len(permutations)
		for k in range(total):

			element = permutations.popleft()
			for i in range(len(element),-1,-1):

				tmp = element[:]
				tmp.insert(i,char)
				permutations.append(tmp)

	return permutations





if __name__ == '__main__':

	s = 'abcd'
	print(allPermutations(s))
