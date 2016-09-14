
'''
Exercise 2.5 – Sum Lists:

You have two numbers, represented by a linked list, where 
each node contains a single digit. The digits are store 
in reverse order, such that the 1’s digit is the head of 
the list. Write a function that adds the two numbers and 
returns the sum as a linked list. 
'''

from LinkedList import LinkedList

def sumList(listA, listB):

	resultList = LinkedList()

	currentA = listA.head
	currentB = listB.head

	carry = 0

	while currentA or currentB:

		total = carry

		if currentA:
			total += currentA.value
			currentA = currentA.next
		if currentB:
			total += currentB.value
			currentB = currentB.next

		carry, result = divmod(total, 10)
		resultList.addElement(result)

	if carry > 0:
		resultList.addElement(carry)

	return resultList


if __name__ == "__main__":

	listA = LinkedList()
	listB = LinkedList()

	listA.addMultiple([7,1,6])
	listB.addMultiple([5,9,2])

	print(sumList(listA,listB))
