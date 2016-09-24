'''
Exercise 4.6 - Successor:

Write an algorithm to find the "next" node of a given node in a binary seach tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.parent = None


def minNode(node):

	while root.left:
		root = root.left
	return root.val

def successorNode(node):

	if node.right:
		return minNode(node.right)

	parent = node.parent

	while parent and parent.right == node:
		node = parent
		parent = parent.parent

	return node

	