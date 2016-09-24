'''
Exercise 4.7 - Build Order:

You are given a list of projects and a list of dependencies. All of a project's 
dependencies must be built before the project is. Find a build order that will 
allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE:
Projects: a, b, c, d, e, f
Dependencies: (d,a) (b,f) (d,b) (a,f) (c,d)
Output: f, e, b, a, d, c
'''

from collections import deque


def buildOrder(graph):

	def dfs(node):
		state[node] = PARTIAL
		for n in graph.get(node,()):
			n_state = state.get(n,())
			if n_state == PARTIAL: raise ValueError('There is a cycle!')
			if n_state == COMPLETED: continue
			nodes.discard(n)
			dfs(n)
		order.appendleft(node)
		state[node] = COMPLETED

	COMPLETED, PARTIAL = 1, 0
	state = {}
	order = deque()
	nodes = set(graph)

	while nodes: dfs(nodes.pop())
	return order

if __name__ == "__main__":

	graph = {
	   	'a': ['d'],
	    'b': ['d'],
	    'c': [],
	    'd': ['c'],
	    'e': [],
	    'f': ['a','b']
	}

	print(buildOrder(graph))