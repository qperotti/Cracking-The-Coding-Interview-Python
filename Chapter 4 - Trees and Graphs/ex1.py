'''
Exercise 4.1 - Route Between Nodes:

Given a directed graph, design an algorithm to find out 
whether there is a route between two nodes.
'''

from collections import deque
from Graph import Graph

def routeBetweenN(start,end):
	
	stack = deque()
	visited = set()

	stack.append(start)
	visited.add(start)

	while stack:
		node = stack.pop()
		if node == end:
			return True
		for neighbor in node.neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				stack.append(neighbor)

	return False




if __name__ == '__main__':

	g = Graph()
	g.addConnection(0,1,False)
	g.addConnection(0,4,False)
	g.addConnection(0,5,False)
	g.addConnection(1,4,False)
	g.addConnection(4,5,True)

	print(routeBetweenN(g.nodes[1],g.nodes[5]))