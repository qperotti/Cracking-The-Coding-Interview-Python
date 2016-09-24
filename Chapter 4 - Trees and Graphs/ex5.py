'''
Exercise 4.5 - Validate BST:

Implement a function to check if a binary tree is a binary search tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



def checkBST(root, minVal, maxVal):
            
            if not root:
                return True
            
            if minVal != None and root.val <= minVal or maxVal != None and root.val >= maxVal:
                return False
            else:
                return checkBST(root.left,minVal,root.val) and checkBST(root.right,root.val,maxVal)

def isValidBST(root):
        
        if not root:
            return True

        minVal = maxVal = None
        return (checkBST(root.left,minVal,root.val) and checkBST(root.right,root.val,maxVal))