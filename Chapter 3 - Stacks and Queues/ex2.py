'''
Exercise 3.2 - Stack Min:

How would you design a stack which, in addition to 
push and pop, has a function min which returns the 
minimum element? Push, pop and min should all operate in O(1). 
'''

class StackMin:

	def __init__(self, size):
		self.size = size
		self.stackSize = 0
		self.stack = [0] * size
		self.minStackSize = 0
		self.minStack = [0] * size

	def push(self, element):
		if self.isFull():
			raise Exception('This Stack is full.')

		self.stack[self.stackSize] = element
		self.stackSize += 1

		if self.minStackSize == 0:
			self.minStack[self.minStackSize] = element
			self.minStackSize += 1
		else:
			if element <= self.minStack[self.minStackSize-1]:
				self.minStack[self.minStackSize] = element
				self.minStackSize += 1


	def pop(self):
		if self.isEmpty():
			raise Exception('This Stack is empty.')

		item = self.stack[self.stackSize-1]
		self.stackSize -= 1

		if item == self.minStack[self.minStackSize-1]:
			self.minStackSize -= 1
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


if __name__ == "__main__":

	myStack = StackMin(10)

	myStack.push(5)
	myStack.push(10)
	myStack.push(6)
	myStack.push(2)
	myStack.push(2)
	myStack.push(45)

	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.pop()

	print(myStack.stack,myStack.minStack)
	print(myStack.top(),myStack.min())

