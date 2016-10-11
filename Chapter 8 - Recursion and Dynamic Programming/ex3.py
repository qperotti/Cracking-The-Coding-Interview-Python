'''
Exercise 8.3 - Magic Index:

A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, 
if one exists, in array A. 

FOLLOW UP: What if the values are not distinct?
'''


def findMagicNumber(A):

	left, right = 0, len(A)-1

	while left <= right:

		mid = (left + right)//2
		
		if A[mid] == mid: return mid

		if mid > A[mid]: left = mid+1
		else: right = mid-1

	return -1


def followUp(A):

	def BSearch(left,right):

		if left > right:
			return -1
		
		mid = (left+right)//2
		if A[mid] == mid:
			return mid

		# Check left
		rightIndex = min(mid-1,A[mid])
		left = BSearch(left,rightIndex)
		if left != -1:
			return left
			
		# Check right 
		leftIndex = max(mid+1,A[mid])
		right = BSearch(leftIndex,right)

		return right

	left, right = 0, len(F)-1
	return BSearch(left, right)


if __name__ == '__main__':

	A = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
	F = [-10,-5,2,2,2,3,4,7,9,12,13]

	print('The magic number is: ' +  str(findMagicNumber(A)))
	print('The magic number is: ' +  str(followUp(F)))
