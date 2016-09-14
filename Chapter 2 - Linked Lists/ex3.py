'''
Exercise 2.3 – Delete Middle Node:

Implement an algorithm to delete a node in the middle 
of a singly linked list, given only access to that node.
'''

from LinkedList import LinkedList

def delMiddleNode(node):

    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
	
	myList = LinkedList()
	myList.addMultiple([1,2,3,4,5,6])
	print(myList)
	# Delete 3
	delMiddleNode(myList.head.next.next)
	print(myList)
