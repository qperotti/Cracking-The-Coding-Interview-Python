'''
Exercise 4.11 - Random Node:

You are implementing a binary search tree class from scratch, which, in 
addition to insert, and find, has a method getRandomNode() which 
returns a random node from the tree. All nodes should be equally likely to be chosen. 
'''
from random import randint

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.size = 1

	def __str__(self):
		return str(self.val)

	def getRandomNode(self):
		leftSize = 0 if self.left == None else self.left.size
		index = randint(0,self.size+1)
		if index < leftSize:
			return self.left.getRandomNode()
		elif index == leftSize:
			return self
		else:
			return self.right.getRandomNode()


	def addElement(self, x):

		if x < self.val:
			if not self.left:
				self.left = TreeNode(x)
			else:
				self.left.addElement(x)
		else:
			if not self.right:
				self.right = TreeNode(x)
			else:
				self.right.addElement(x)
		self.size += 1


	def findElement(self,x):
		if self.val == x:
			return self
		elif self.val > x:
			return None if not self.left else self.left.findElement(x)
		elif self.val < x:
			return None if not self.right else self.right.findElement(x)

