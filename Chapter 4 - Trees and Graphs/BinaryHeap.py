from random import randint

# Binary MinHeap

class BinaryHeap:

	def __init__(self):
		self.nodes = []
		self.total_nodes = 0

	def add(self,element):

		def addHeapify(index):
			if self.nodes[index//2] > self.nodes[index]:
				self.nodes[index//2], self.nodes[index] = self.nodes[index], self.nodes[index//2]
				addHeapify(index//2)

		self.nodes.append(element)
		addHeapify(self.total_nodes)
		self.total_nodes += 1



	def pop(self):

		def popHeapify(index):
			left = (index * 2) + 1
			right = (index * 2) + 2
			min_val = index

			if left < self.total_nodes and self.nodes[left] < self.nodes[min_val]:
				min_val = left
			if right < self.total_nodes and self.nodes[right] < self.nodes[min_val]:
				min_val = right

			if min_val != index:
				self.nodes[min_val], self.nodes[index] = self.nodes[index], self.nodes[min_val]
				popHeapify(min_val)


		if self.empty():
			return

		element = self.nodes[0]
		self.nodes[0], self.nodes[self.total_nodes-1] = self.nodes[self.total_nodes-1], self.nodes[0]
		self.nodes.pop()
		self.total_nodes -= 1
		popHeapify(0)
		
		return element

	

	def empty(self):
		return self.total_nodes < 1


if __name__ == "__main__":

	m = BinaryHeap()
	
	for _ in range(10):
		m.add(randint(1,1000))

	while not m.empty():
		print(m.pop(), end=' ')
	print('')

