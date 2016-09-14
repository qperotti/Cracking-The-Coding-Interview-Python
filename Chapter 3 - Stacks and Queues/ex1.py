'''
Exercise 3.1 - Three in One:

Describe how you could use a single array to implement three stacks. 
'''

class ThreeInOne:

	def __init__(self, size):
		self.size = size
		self.stack = [0] * size * 3
		self.stackSize = [0] * 3

	def push(self, stackNumber, element):
		if self.isFull(stackNumber):
			raise Exception('This Stack is full.')

		position = (stackNumber - 1) * 3 + self.stackSize[stackNumber-1]
		self.stack[position] = element
		self.stackSize[stackNumber-1] += 1

	def pop(self, stackNumber):
		if self.isEmpty(stackNumber):
			raise Exception('This Stack is empty.')

		position = (stackNumber - 1) * 3 + self.stackSize[stackNumber-1] -1
		item = self.stack[position]
		self.stackSize[stackNumber-1] -= 1
		return item


	def isEmpty(self, stackNumber):
		if self.stackSize[stackNumber-1] == 0:
			return True
		return False

	def isFull(self, stackNumber):
		if self.stackSize[stackNumber-1] >= self.size:
			return True
		return False

	def top(self, stackNumber):
		if self.isEmpty(stackNumber):
			raise Exception('This Stack is empty.')

		position = (stackNumber - 1) * 3 + self.stackSize[stackNumber-1] -1
		return self.stack[position]

