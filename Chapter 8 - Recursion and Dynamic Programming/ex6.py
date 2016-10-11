'''
Exercise 8.6 - Towers of Hanoi:

Write a program to move the disks from the first tower to the last using Stacks.
'''

from collections import deque

class Tower():
		
		def __init__(self, index):
			self.index = index
			self.disks = deque()

		def __repr__(self):
			tower = 'Tower: ' + str(self.index) + '\n'
			for i in range(len(self.disks)):
				tower += str(self.disks[i]) + '\n'
			return tower

		def addDisk(self, disk):
			self.disks.append(disk)

		def moveTopTo(self, tower):
			tower.addDisk(self.disks.pop())

		def moveDisks(self, n, towerDest, towerBuff):
			if n > 0:
				self.moveDisks(n-1, towerBuff, towerDest)
				self.moveTopTo(towerDest)
				towerBuff.moveDisks(n-1,towerDest,self)



if __name__ == '__main__':

	n = 3
	towers = [ Tower(i) for i in range(3) ]

	for i in range(4):
		towers[0].addDisk(i)

	towers[0].moveDisks(4,towers[2],towers[1])
	print(towers[2])






