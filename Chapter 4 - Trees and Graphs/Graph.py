# Adjaceny List Graph
from collections import defaultdict, deque

class Node:
	def __init__(self, x=None):
		self.label = x
		self.neighbors = []


class Graph:
	def __init__(self):
		self.nodes = defaultdict(Node)


	def addConnection(self, origin, destination, undirected):
		
		origNode = self.nodes[origin]
		if not origNode.label: origNode.label=origin
		# This means that origin node is a New Node

		destNode = self.nodes[destination]
		if not destNode.label: destNode.label=destination
		# This means that destination node is a New Node

		origNode.neighbors.append(destNode)
		if undirected:
			destNode.neighbors.append(origNode)


	def deleteNode(self,x):
		if x not in self.nodes:
			print("This node does not exist.")
		
		for key,node in self.nodes.items():
			for i in range(len(node.neighbors)):
				if node.neighbors[i].label == x:
					node.neighbors.pop(i)
					break
		
		del self.nodes[x]


	def traversalDFS(self,start):
		# DFS Recurvise

		def DFS(x,visited):

			print(x.label)
			for neighbor in x.neighbors:
				if neighbor not in visited:
					visited.add(neighbor)
					DFS(neighbor,visited)

		if start not in self.nodes:
			return

		visited = set()
		visited.add(self.nodes[start])
		DFS(self.nodes[start],visited)

	def traversalBFS(self,start):

		if start not in self.nodes:
			return

		queue = deque()
		visited = set()

		queue.append(self.nodes[start])
		visited.add(self.nodes[start])

		while queue:

			node = queue.popleft()
			print(node.label)

			for neighbor in node.neighbors:
				if neighbor not in visited:
					visited.add(neighbor)
					queue.append(neighbor)


if __name__ == "__main__":
	g = Graph()
	g.addConnection(0,1,True)
	g.addConnection(0,4,True)
	g.addConnection(0,5,True)
	g.addConnection(1,4,True)
	g.addConnection(4,5,True)

	
	Graph()
	g.traversalBFS(0)
	print("")
	g.deleteNode(4)
	g.traversalBFS(0)


