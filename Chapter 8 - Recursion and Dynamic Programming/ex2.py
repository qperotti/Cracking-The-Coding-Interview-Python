'''
Exercise 8.2 - Robot in a Grid:

Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are 
"off limits" such that the robot cannot step on them. Design an algorithm to find 
a path for the robot from the top left to the bottom right.
'''

from collections import deque


def getPath(maze):

	maxR, maxC = len(maze), len(maze[0])
	
	path = dict()
	queue = deque()
	
	start = (0,0)
	path[start] = None

	queue.append(start)

	while queue:

		r,c = queue.popleft()

		if maze[r][c] == 'E':
			print('Found')
			break

		if r-1 > 0 and maze[r-1][c] != '|' and (r-1,c) not in path:
			queue.append((r-1,c))
			path[(r-1,c)] = (r,c)
		elif r+1 < maxR and maze[r+1][c] != '|' and (r+1,c) not in path:	
			queue.append((r+1,c))
			path[(r+1,c)] = (r,c)
		if c-1 > 0 and maze[r][c-1] != '|' and (r,c-1) not in path:
			queue.append((r,c-1))
			path[(r,c-1)] = (r,c)
		elif c+1 < maxC and maze[r][c+1] != '|' and (r,c+1) not in path:	
			queue.append((r,c+1))
			path[(r,c+1)] = (r,c)
	
	return path




if __name__ == '__main__':

	maze = [['S',' ',' ',' ','|','|',' '],
			[' ',' ',' ',' ','|','|',' '],
			[' ','|','|',' ','|','|',' '],
			[' ','|','|',' ','|','|',' '],
			[' ','|','|',' ','|','|',' '],
			[' ','|','|',' ',' ',' ',' '],
			[' ','|','|',' ',' ',' ',' '],
			[' ',' ',' ',' ','|','|',' '],
			[' ',' ',' ',' ','|','|',' '],
			[' ',' ',' ',' ','|','|',' '],
			[' ',' ',' ',' ','|','|','E']]

	path = getPath(maze)
	end = (len(maze)-1,len(maze[0])-1)
	pos = path[end]
	
	# Print the path
	while pos != None:
		r,c = pos
		maze[r][c] = 'O'
		pos = path[pos]

	for r in maze: print(r)
















