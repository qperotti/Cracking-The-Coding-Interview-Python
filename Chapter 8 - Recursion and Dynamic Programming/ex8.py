'''
Exercise 8.8 - Permutations with Duplicates:

Write a method to compute all permutations of a string whose characters 
are not necessarily unique. The list of permutations should not have duplicates.
'''

def allPermutations(S):
	freqMap = getFreqMap(S)
	result = []
	printPerms(freqMap,'',len(S),result)
	return result



def printPerms(freqMap, prefix, remaining, result):
	
	# Base case
	if remaining == 0:
		result.append(prefix)
		return

	for key in freqMap:
		count = freqMap[key]
		if count > 0:
			freqMap[key] = count-1
			printPerms(freqMap,prefix+key,remaining-1,result)
			freqMap[key] = count



def getFreqMap(S):

	freqMap = dict()

	for char in S:
		if char not in freqMap:
			freqMap[char] = 1
		else:
			freqMap[char] += 1

	return freqMap




if __name__ == '__main__':

	s = 'abbc'
	print(allPermutations(s))
