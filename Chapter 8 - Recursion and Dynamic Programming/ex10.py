'''
Exercise 8.10 - Paint Fill:

Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point , and 
a new color, fill in the surrounding area until the color changes from the origial color.
'''

from collections import deque




def paintFill(image, r, c, newColor):

	visited = set()
	queue = deque()

	currentColor = image[r][c]
	maxR, maxC = len(image), len(image[0])

	visited.add((r,c))
	queue.append((r,c))

	print(maxR,maxC,currentColor)

	while queue:

		r,c = queue.popleft()
		image[r][c] = newColor

		if r-1 > 0 and image[r-1][c] == currentColor and (r-1,c) not in visited:
			queue.append((r-1,c))
			visited.add((r-1,c))
		elif r+1 < maxR and image[r+1][c] == currentColor and (r+1,c) not in visited:	
			queue.append((r+1,c))
			visited.add((r+1,c))
		if c-1 > 0 and image[r][c-1] == currentColor and (r,c-1) not in visited:
			queue.append((r,c-1))
			visited.add((r,c-1))
		elif c+1 < maxC and image[r][c+1] == currentColor and (r,c+1) not in visited:	
			queue.append((r,c+1))
			visited.add((r,c+1))
		




if __name__ == '__main__':

	'''
	B = Blue
	G = Green
	O = Orange
	X = newColor
	'''

	image = [
			['O','O','O','O','G','G','B'],
			['O','O','O','O','G','G','B'],
			['O','G','G','O','G','G','B'],
			['O','G','G','O','G','G','B'],
			['O','G','G','O','G','G','B'],
			['O','G','G','O','B','B','B'],
			['O','G','G','O','B','B','B'],
			['O','O','O','O','G','G','B'],
			['O','O','O','O','G','G','B'],
			['O','O','O','O','G','G','B'],
			['O','O','O','O','G','G','B']]

	paintFill(image,0,0,'X')

	for r in image: print(r)




