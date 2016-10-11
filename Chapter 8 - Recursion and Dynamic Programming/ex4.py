'''
Exercise 8.4 - Write a method to return all subsets of a set.
'''

def powerSet(S):

	sets = [[]]

	for element in S:

		total = len(sets)
		for i in range(total):
			sets.append(sets[i] + [element])

	return sets





if __name__ == '__main__':

	s = [1,2,3,4]
	print(powerSet(s))
