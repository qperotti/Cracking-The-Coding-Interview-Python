'''
Exercise 10.1 - Sorted Merge:

You are given two sorted arrays, A and B, and A has a 
large enough buffer at the end to hold B. Write a method 
to merge B into A in sorted order.
'''

def sortedMerge(listA, listB):
	indexSort = len(listA)-1
	indexA = len(listA) - len(listB) -1
	indexB = len(listB)-1

	while indexB >= 0:
		if listA[indexA] > listB[indexB]:
			listA[indexSort] = listA[indexA]
			indexA -= 1
		else:
			listA[indexSort] = listB[indexB]
			indexB -= 1
		indexSort -= 1



listA = [1,3,5,7,9,0,0,0,0]
listB = [2,4,6,8]

sortedMerge(listA,listB)
print(listA)