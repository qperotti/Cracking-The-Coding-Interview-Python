'''
Exercise 4.3 - List of Depths:

Given a binary tree, design an algorithm which 
creates a linked list of all the nodes at each depth.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def listofDepths(root):

	if not root:
		return []

	lvlList = []
	lvl = 0
	queue = deque()
	queue.append((root,lvl))


	while queue:
		node, lvl = queue.popleft()

		if len(lvlList) == lvl:
			lvlList.append([])
		lvlList[lvl].append(node.val)
		lvl +=1

		if node.left:
			queue.append((node.left,lvl))
		if node.right:
			queue.append((node.right,lvl))

	return lvlList

def testTree():

	def addNode(x,lvl):
		if lvl > 4:
			return None
		root = TreeNode(x)
		root.left = addNode(x*2,lvl+1)
		root.right = addNode(x*2+1,lvl+1)

		return root

	return addNode(1,1)

if __name__ == '__main__':
	
	root = testTree()
	print(listofDepths(root))
