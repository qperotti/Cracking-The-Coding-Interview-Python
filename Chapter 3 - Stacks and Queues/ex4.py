'''
Exercise 3.4 - Queue via Stacks:

Implement a MyQueue class which implements a queue using two stacks. 
'''

from Stack import Stack

class QueueViaStacks:

	def __init__(self,size):
		self.size = size
		self.stack1 = Stack(size)
		self.stack2 = Stack(size)
		# Mode = 1 means items in Stack1 //Push()
		# Mode = 2 means items in Stack2 //Pop()
		self.mode = 1
		self.elements = 0

	def push(self, element):
		if self.isFull():
			raise Exception('This Stack is full.')
		if self.mode == 2:
			self.reverseMod()

		self.stack1.push(element)
		self.elements += 1

	def pop(self):
		if self.isEmpty():
			raise Exception('This Stack is empty.')
		if self.mode == 1:
			self.reverseMod()

		item = self.stack2.pop()
		self.elements -= 1
		return item


	def reverseMod(self):
		if self.mode == 1:
			self.mode = 2
			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())
		else:
			self.mode = 1
			while not self.stack2.isEmpty():
				self.stack1.push(self.stack2.pop())


	def isFull(self):
		if self.elements >= self.size:
			return True
		return False

	def isEmpty(self):
		if self.elements == 0:
			return True
		return False


if __name__ == "__main__":

	myQueue = QueueViaStacks(10)
	myQueue.push(1)
	myQueue.push(2)
	myQueue.push(3)
	myQueue.push(4)
	print(myQueue.pop(),myQueue.pop())
	myQueue.push(1)
	print(myQueue.pop(),myQueue.pop())








