
'''
Exercise 2.6 – Palindrome:

Implement a function to check if a linked list is a palindrome.
'''


from LinkedList import LinkedList
from collections import deque

def isPalindrome(myList):
	current = runner = myList.head
	stack = deque()

	while runner != None:
		stack.append(current.value)
		current = current.next
		runner = runner.next
		if runner:
			runner = runner.next
		else:
			# In the case the list is even we need to pop the middle element
			stack.pop()

	while current != None:
		if current.value != stack.pop():
			return False
		current = current.next

	return True


if __name__ == "__main__":

	myList = LinkedList()
	myList.addMultiple([1,2,3,4,3,2,1])
	print(isPalindrome(myList))

