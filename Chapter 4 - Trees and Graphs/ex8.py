'''
Exercise 4.8 - First Common Ancestor:

Design an algorithm and write code to find the first common ancestor of 
two nodes in a binary tree. Avoid storing additional nodes in a data structure.
'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Result:
	def __init__(self, x, isAncestor):
		self.node = TreeNode(x)
		self.isAncestor = isAncestor

def commonAncestor(root,p,q):
	
	result = commonAncestorHelper(root,p,q)
	if result.isAncestor:
		return result.node
	return None	

def commonAncestorHelper(root,p,q):

	if root == None: 
		return Result(None,False)

	if root == p or root == q:
		return Result(root,True)

	rLeft = commonAncestorHelper(root.left,p,q)
	if rLeft.isAncestor:
		return rLeft

	rRight = commonAncestorHelper(root.right,p,q)
	if rRight.isAncestor:
		return rRight

	if rLeft.node != None and rRight.node != None:
		return Result(root,True)
	elif root == p or root == q:
		return Result(root,rLeft.node != None or rRight.node != None)
	else:
		if rLeft.node != None:
			return Result(rLeft.node ,False)
		else:
			return Result(rRight.node ,False)