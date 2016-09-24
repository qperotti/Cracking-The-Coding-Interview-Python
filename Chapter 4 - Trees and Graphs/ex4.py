'''
Exercise 4.4 - Check Balanced:

Implement a function to check if a binary tree is balanced 
(the heights of the two subtrees of any node never differ by more than one).
'''


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def dfs(root):
        
        if not root:
            return 0
            
        leftDepth = dfs(root.left)
        if leftDepth == -1: return -1
        rightDepth = dfs(root.right)
        if rightDepth == -1: return -1
    
        return -1 if abs(leftDepth - rightDepth) > 1 else max(leftDepth,rightDepth)+1


def isBalanced(root):

    if not root:
        return True
    
    return dfs(root) != -1


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
	print(isBalanced(root))