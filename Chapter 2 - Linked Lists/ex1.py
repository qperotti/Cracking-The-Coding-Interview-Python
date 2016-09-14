'''
Exercise 2.1 - Remove Dups:

Write code to remove duplicates from an unsorted linked list.
Follow Up: How would you solve this problem if a temporary buffer is not allowed?
'''

from LinkedList import LinkedList


def removeDups(myList):
	if myList.head == None:
		return 

	current = myList.head
	viewed = set()
	viewed.add(current.value)

	while current.next != None:
		if current.next.value in viewed:
			current.next = current.next.next
		else:
			viewed.add(current.next.value)
			current = current.next


def removeDups_noDS(myList):
	if myList.head == None:
		return 

	current = myList.head

	while current.next != None:
		runner = current
		while runner.next != None:
			if runner.next.value == current.value:
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next





if __name__ == "__main__":

	myList = LinkedList()
	myList.addMultiple([1,2,1,4,1,6])

	print(myList)
	removeDups_noDS(myList)
	print(myList)
