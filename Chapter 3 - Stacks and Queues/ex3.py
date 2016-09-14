'''
Exercise 3.3 - Stack of Plates:

Implement SetOfStacks. This DS should be composed of 
several stacks and should create a new stack once the 
previous one exceeds capacity. 
'''

from Stack import Stack

class SetOfStacks:

	def __init__(self,sizeOfStacks):
		self.size = sizeOfStacks
		self.arrayStacks = []
		self.totalStacks = 0

	def push(self, element):

		if self.isEmpty():
			self.arrayStacks.append(Stack(self.size))
			self.totalStacks = 1

		currentStack = self.arrayStacks[self.totalStacks-1]
		currentStack.push(element)
		if currentStack.isFull():
			self.arrayStacks.append(Stack(self.size))
			self.totalStacks += 1

	def pop(self):
		if self.isEmpty():
			raise Exception('This Stack is empty.')

		currentStack = self.arrayStacks[self.totalStacks-1]
		element = currentStack.pop()
		if currentStack.isEmpty():
			del self.arrayStacks[self.totalStacks-1]
			self.totalStacks -= 1
		return element

	def isEmpty(self):
		if self.totalStacks == 0:
			return True
		return False


if __name__ == "__main__":

	myStack = SetOfStacks(2)
	myStack.push(1)
	myStack.push(2)
	myStack.push(3)
	myStack.push(4)
	myStack.push(5)

	while not myStack.isEmpty():
		print(myStack.pop())