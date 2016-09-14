'''
Exercise 3.5 - Sort Stacks:

Write a program to sort a stack such that the smallest items 
are on the top. You can use an additional temporary stack, 
but you may not copy the elements into any other data structure. 
'''

from Stack import Stack

def SortStack(myStack):
	tmpStack = Stack(10)
	tmp = None
	# Number of items not sorted in the Stack
	items = myStack.stackSize

	while items > 0:

		# We pop our stack to find the biggest not sorted element 
		# each time
		for _ in range(items):
			element = myStack.pop()
			if tmp == None:
				tmp = element
			else:
				if tmp < element:
					tmpStack.push(tmp)
					tmp = element
				else:
					tmpStack.push(element)

		myStack.push(tmp)

		while not tmpStack.isEmpty():
			myStack.push(tmpStack.pop())

		items -= 1
		tmp = None
		
		print(myStack.stack)


if __name__ == "__main__":
	
	myStack = Stack(10)
	myStack.push(8)
	myStack.push(2)
	myStack.push(5)
	myStack.push(9)
	myStack.push(100)
	myStack.push(1)
	SortStack(myStack)
