'''
Exercise 4.10 - Check Subtree:

T1 and T2 are two vary large binary trees, with T1 much bigger
than T2. Create an algorithm to determine if T2 is a subtree of T1.
'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def isSameTree(t1,t2):
	if t1 and t2:
		return t1.val == t2.val and isSameTree(t1.left,t2.left) and isSameTree(t1.right,t1.right)
	return t1 is t2

def checkSubtree(t1,t2):

	if not t1:
		return False
	elif t1.val == t2.val and isSameTree(t1,t2):
		return True

	return checkSubtree(t1.left,t2) or checkSubtree(t1.right,t2)