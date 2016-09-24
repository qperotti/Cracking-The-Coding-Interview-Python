'''
Exercise 4.2 - Minimal Tree:

Given a sorted array with unique integer elements, write 
an algorithm to create a binary search tree with minimal height.
'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def sortedArrayToBST(self, nums):
    
    if not nums:
        return None
    
    mid = (len(nums)-1)//2
    
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root