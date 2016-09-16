'''
Exercise 10.2 - Group Anagrams:

Write a method to sort an array of string so that all 
the anagrams are next to each other. 
'''

from collections import defaultdict

def groupAnagrams(myList):
	
	myMap = defaultdict(list)

	for item in myList:
		key = ''.join(sorted(item))
		myMap[key].append(item)

	index = 0
	for key in myMap:
		for item in myMap[key]:
			myList[index] = item
			index += 1

if __name__ == "__main__":

	myList = ['hello','world','dog','holel','god','rldwo','lasdasd']
	groupAnagrams(myList)
	print(myList)