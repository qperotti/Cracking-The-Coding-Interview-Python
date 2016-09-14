
'''
Exercise 2.4 – Partition:

Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes 
greater than or equal to x. 
'''

from LinkedList import LinkedList

def partition(myList, partition):

    smallHead = smallTail = bigHead = None
    current = myList.head

    while current != None:
    	nextNode = current.next
    	current.next = None
    	if(current.value < partition):
    		if not smallHead:
    			smallHead = smallTail = current
    		else:
    			current.next = smallHead
    			smallHead = current
    	else:
    		if bigHead:
   				current.next = bigHead
    		bigHead = current

    	current = nextNode

    smallTail.next = bigHead
    
    # Return head of new list
    return smallHead




if __name__ == "__main__":

    myList = LinkedList()
    myList.addRandom(1,100,10)
    print(myList)
    print(partition(myList,myList.head.value))
