from random import randint

class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __str__(self):
	    return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None

	def __iter__(self):
	    current = self.head
	    while current:
	        yield current
	        current = current.next

	def __str__(self):
	    values = [str(x) for x in self]
	    return ' -> '.join(values)

	def __len__(self):
	    result = 0
	    node = self.head
	    while node:
	        result += 1
	        node = node.next
	    return result

	def addNode(self,node):
		if self.head == None:
			self.head = node
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = node		

	def addElement(self,value):

		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = Node(value)

	def addRandom(self,min_val,max_val,total):
		for _ in range(total):
			self.addElement(randint(min_val, max_val))

	def addMultiple(self, values):
	    for v in values:
	        self.addElement(v)

