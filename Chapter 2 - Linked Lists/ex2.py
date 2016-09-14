'''
Exercise 2.2 – Return Kth to Last:

Implement an algorithm to find the Kth to last element 
of a singly linked list.
'''

from LinkedList import LinkedList

# Revursive
def recursiveKth(node,k):
	if node == None:
		return 1, None

	position, kvalue = recursiveKth(node.next,k)
	
	if position == k:
		return position+1, node.value
	
	return position+1,kvalue

def returnKthR(myList,k):
	position, kvalue = recursiveKth(myList.head,k)
	return kvalue


# Iterative
def returnKthI(myList,k):

	current = runner = myList.head
	for _ in range(k):
		if runner == None:
			return None
		runner = runner.next

	while runner != None:
		runner = runner.next
		current = current.next

	return current.value



if __name__ == "__main__":
	
	myList = LinkedList()
	myList.addRandom(1,100,10)
	print(myList)
	print(returnKthI(myList,3))

