'''
Exercise 1.8 - Zero Matrix:

Write an algorithm such that if an element in an MxN matrix 
is 0, its entire row and column are set to 0.
'''

def zeroRow(matrix,row):
	for r in row:
		for c in range(len(matrix[r])):
			matrix[r][c] = 0

def zeroColumn(matrix,column):
	for c in column:
		for r in range(len(matrix)):
			matrix[r][c] = 0

def zeroMatrix(matrix):

	row = set()
	column = set()

	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if matrix[r][c] == 0:
				row.add(r)
				column.add(c)

	zeroRow(matrix, row)
	zeroColumn(matrix, column)

	return matrix
	

if __name__ == "__main__":

	matrix =[[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 0, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 0, 25]]

	# Test
	print(zeroMatrix(matrix))
