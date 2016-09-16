'''
Exercise 10.9 - Sorted Matrix Search:

Given an M x N matrix in which each row and each column is sorted 
in ascending order, write a method to find an element.

'''

def binarySearch(myList,target,start,end):
	
	while start <= end:
		middle = (start + end)//2
		if myList[middle] == target:
			return middle

		if target < myList[middle] or myList[middle] == -1:
			end = middle-1
		else:
			start = middle+1

	return -1

def sortedMatrixSearch(matrix, target):

	for row in range(len(matrix)):
		if target >= matrix[row][0] and target <= matrix[row][len(matrix)-1]:
			column = binarySearch(matrix[row],target,0,len(matrix)-1)
			if column != -1:
				return row,column
	return -1,-1



if __name__ == "__main__":

	matrix =[[1, 2, 3, 4, 5],
	         [6, 7, 8, 9, 10],
	         [11, 12, 13, 14, 15],
	         [16, 17, 18, 19, 20],
	         [21, 22, 23, 24, 25]]

	# Test
	print(sortedMatrixSearch(matrix,13))
