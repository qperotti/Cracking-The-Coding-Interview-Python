'''
Exercise 1.7 - Rotate Matrix:

Given an imagen represented by an NxN matrix, where each pixel 
in the image is 4 bytes, wrtie a method to rotate the image 90 degrees. 
Can you do this in place?
'''


def rotateMatrix(matrix):
	for row in range(len(matrix)//2):
		
		length = len(matrix)
		first, last = row, length - row - 1

		for index in range(last-first):
				

			# save top-left
			temp = matrix[first][first+index]

			# top-left = bottom-left
			matrix[first][first+index] = matrix[last-index][first]

			# bottom-left = bottom-right
			matrix[last-index][first] = matrix[last][last-index]

			#bottom-right = top-right
			matrix[last][last-index] = matrix[first+index][last]

			#top-right = top-left
			matrix[first+index][last] = temp

	return matrix


if __name__ == "__main__":

	matrix =[[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]

	# Test
	print(rotateMatrix(matrix))
