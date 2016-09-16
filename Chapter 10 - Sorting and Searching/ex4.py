'''
Exercise 10.4 - Sorted Search, No Size:

You are given an array-like data structure Listy which lacks 
a size method. It does, however, have an elementAt(i) method 
that returns the element at index i in O(1) time. If i is beyond 
the bounds of the data structure, it returns -1. (For this reason, 
the data structure only supports positive integers.) Given a Listy 
which contains sorted, positive integers, find the index at which an 
element x occurs. If x occurs multiple times, you may return any index.

'''

def findLength(myList,target):
	index = 1
	while myList[index-1] != -1 and myList[index-1] <= target:
		index *= 2
	return index-1


def tweakBS(myList,target,start,end):
	
	while start <= end:
		middle = (start + end)//2
		if myList[middle] == target:
			return middle

		if target < myList[middle] or myList[middle] == -1:
			end = middle-1
		else:
			start = middle+1

	return -1


def sortedSearch_noSize(myList,target):
	length = findLength(myList,target)
	return tweakBS(myList,target,0,length)


if __name__ == "__main__":

	myList = [1,2,4,5,6,10,23,25,100,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
	print(sortedSearch_noSize(myList,100))