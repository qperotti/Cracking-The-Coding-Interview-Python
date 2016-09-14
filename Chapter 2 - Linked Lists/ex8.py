
'''
Exercise 2.8 – Loop Detection:

Given a circular linked list, implement an algorithm that 
returns the node at the beginning of the loop. 
'''

from LinkedList import LinkedList, Node

def loopDetection(myList):


    slow = runner = myList.head

    while runner and runner.next:

        slow = slow.next
        runner = runner.next.next

        if slow == runner:

            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next

            return slow

    return None