from collections import deque


class node:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right



def insertNode(root,val):

	if not root:
		root = node(val)
	else:
		if val > root.val:
			if not root.right:
				root.right = node(val)
			else:
				insertNode(root.right,val)
		if val < root.val:
			if not root.left:
				root.left = node(val)
			else:
				insertNode(root.left,val)

def findNode(root,val):

	if not root:
		return False

	if root.val == val:
		return True

	return findNode(root.right,val) if root.val < val else findNode(root.left,val)

#########################################
# Delete Node
#########################################


def findMinNode(root):
	while root.left:
		root = root.left
	return root.val

def deleteNode(root,val):
	if not root:
		return

	if root.val == val:
		
		# Here is the fun stuff
		if not root.left and not root.right:
			return None
		elif root.left and not root.right:
			return root.left
		elif not root.left and root.right:
			return root.right
		else:
			minVal = findMinNode(root.right)
			root.val = minVal
			root.right = deleteNode(root.right,minVal)
			return root
	else:

		if root.val < val:
			root.right = deleteNode(root.right,val)
		else:
			root.left = deleteNode(root.left,val)
		return root

#########################################
# Tree Traversal **_Recursive_**
#########################################

def inOrderTraversal(root):
	if root:
		inOrderTraversal(root.left)
		print(root.val, end=' ')
		inOrderTraversal(root.right)

def preOrderTraversal(root):
	if root:
		print(root.val, end=' ')
		preOrderTraversal(root.left)
		preOrderTraversal(root.right)

def postOrderTraversal(root):
	if root:
		postOrderTraversal(root.left)
		postOrderTraversal(root.right)
		print(root.val, end=' ')

#########################################
# Tree Traversal Iterative **_Iterative__**
#########################################

def inOrderTraversal_I(root):

	stack = deque()

	while stack or root:

		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			print(root.val, end=' ')
			root = root.right


def preOrderTraversal_I(root):
	
	stack = deque()

	while stack or root:

		if root:
			print(root.val, end=' ')
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			root = root.right


def postOrderTraversal_I(root,stacks):

	# Two Stacks
	if stacks == 2:
		stack = deque()
		postStack = deque()

		while stack or root:
			if root:
				postStack.append(root.val)
				stack.append(root)
				root = root.right
			else:
				root = stack.pop()
				root = root.left

		while postStack:
			print(postStack.pop(), end=' ')

	# One Stack
	if stacks == 1:
		stack = deque()
		while stack or root:
			if root:
				stack.append(root)
				if root.right:
					stack.append(root.right)
				root = root.left
			else:
				root = stack.pop()
				if stack and root.val == stack[0].val:
					stack.pop()
					stack.append(root)
					root = root.right
				else:
					print(root.val, end=' ')
					root = None

def levelTraversal(root):


	if root:
		queue = deque()
		queue.append(root)

		while queue:
			root = queue.popleft()
			print(root.val, end=' ')

			if root.left:
				queue.append(root.left)
			if root.right:
				queue.append(root.right)


#########################################


if __name__ == "__main__":

	root = node(50)
	insertNode(root,25)
	insertNode(root,75)
	insertNode(root,15)
	insertNode(root,30)
	insertNode(root,1)
	insertNode(root,20)
	insertNode(root,40)

	levelTraversal(root)
	print("")
	deleteNode(root,15)
	levelTraversal(root)
	print("")









