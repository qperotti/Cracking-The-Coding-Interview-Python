
'''
Exercise 2.7 – Intersection:

Given two linked list, determine if the two lists intersect. 
Return the intersecting node. Note that the intersection is 
defined based on reference, not value. 
'''

from LinkedList import LinkedList

def isIntersection(listA,listB):

	# Calculate lenght A
	currentA = listA.head
	currentB = listB.head

	print(len(listA),len(listB))

	if len(listA) > len(listB):
		for _ in range(len(listA)-len(listB)):
			currentA = currentA.next

	if len(listB) > len(listA):
		for _ in range(len(listB)-len(listA)):
			currentB = currentB.next

	while currentA != None:
		if currentA is currentB:
			return currentA
		currentA = currentA.next
		currentB = currentB.next

	return None



if __name__ == "__main__":

	listA = LinkedList()
	listB = LinkedList()
	l3 = LinkedList()

	listA.addMultiple([3,1,5,9])
	listB.addMultiple([4,6])
	l3.addMultiple([7,2,1])

	listA.addNode(l3.head)
	listB.addNode(l3.head)

	print(isIntersection(listA,listB))
