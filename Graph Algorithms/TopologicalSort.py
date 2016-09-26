'''
Topological Sort Algorithm
Time Complexity: O(V+E)
'''

from collections import deque

COMPLETED, PARTIAL = 1, 0


def topologicalSort(graph):

	def topologicalSortHelp(node):
		
		state[node] = PARTIAL
		for n in graph.get(node,[]):
			nState = state.get(n,())
			if nState == PARTIAL: raise NameError('Cycle!')
			if nState == COMPLETED: continue
			unvisited.discard(n)
			topologicalSortHelp(n)
		state[node] = COMPLETED
		queue.appendleft(node)


	state = dict()
	unvisited = set(graph)
	queue = deque()

	while unvisited: 
		topologicalSortHelp(unvisited.pop())

	return queue

if __name__ == "__main__":

	graph = {
	   	'a': ['d'],
	    'b': ['d'],
	    'c': [],
	    'd': ['c'],
	    'e': [],
	    'f': ['a','b']
	}

	print(topologicalSort(graph))