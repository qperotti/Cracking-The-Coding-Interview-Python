'''
Exercise 4.12 - Path with Sum:

You are given a binary tree in which each node contains an integer value. Design 
an algorithm to count the number of paths that sum to a given value. The path does 
not need to start or end at the root or a leaf.
'''


def incrementCount(pathCount, currentSum, increment):
	newCount = pathCount.get(currentSum,0) + increment
	if newCount == 0:
		del pathCount[currentSum] # Remove the key
	else:
		pathCount[currentSum] = newCount


def countPathHelp(root, targetSum, currentSum, pathCount):

	if not root:
		return 0

	currentSum += root.val
	totalPath = pathCount.get(currentSum - targetSum,0)

	if currentSum == targetSum:
		totalPath +=1

	incrementCount(pathCount,currentSum,1)
	totalPath += countPathHelp(root.left, targetSum, currentSum, pathCount)
	totalPath += countPathHelp(root.right, targetSum, currentSum, pathCount)
	incrementCount(pathCount,currentSum,-1) # Remove runningSum

	return totalPath


def countPath(root,targetSum):
	return countPathHelp(root, targetSum, 0, dict())

