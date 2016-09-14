class Stack:

	def __init__(self, size):
		self.size = size
		self.stackSize = 0
		self.stack = [0] * size

	def push(self, element):
		if self.isFull():
			raise Exception('This Stack is full.')

		self.stack[self.stackSize] = element
		self.stackSize += 1

	def pop(self):
		if self.isEmpty():
			raise Exception('This Stack is empty.')

		item = self.stack[self.stackSize-1]
		self.stackSize -= 1
		return item

	def min(self):
		return self.minStack[self.minStackSize-1]

	def isEmpty(self):
		if self.stackSize == 0:
			return True
		return False

	def isFull(self):
		if self.stackSize >= self.size:
			return True
		return False

	def top(self):
		if self.isEmpty():
			raise Exception('This Stack is empty.')
		return self.stack[self.stackSize-1]

	def getCurrentSize(self):
		return self.stackSize

