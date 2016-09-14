'''
Exercise 3.6 - Animal Shelter:

An animal shelter holds only dogs and cats, and operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" 
(based on arrival time) of all animals at the shelter, or they can 
select whether they would prefer a dog or a cat (and will receive 
the oldest animal of that type). They cannot select which specific 
animal they would like. Create the data structures to maintain this 
system and implement operations such as enqueue, dequeueAny, dequeueDog 
and dequeueCat.
'''

from collections import deque
import datetime

class Animal:
	def __init__(self, name, categorie):
		self.name = name
		self.categorie = categorie
		self.added = str(datetime.datetime.now())

	def getAdded(self):
		return self.added

class AnimalShelter:
	def __init__(self):
		self.dogList = deque()
		self.catList = deque()

	def enqueue(self, name, categorie):
		animal = Animal(name,categorie)
		if categorie == 'dog':
			self.dogList.append(animal)
		else:
			self.catList.append(animal)

	def dequeueDog(self):
		if not self.dogList:
			raise Exception('There are no more dogs!')
		return self.dogList.popleft()

	def dequeueCat(self):
		if not self.catList:
			raise Exception('There are no more cats!')
		return self.catList.popleft()

	def dequeueAny(self):
		if not self.catList and not self.dogList:
			raise Exception('There are no more animals!')
		elif not self.catList and self.dogList:
			return self.dogList.popleft()
		elif self.catList and not self.dogList:
			return self.catList.popleft()
		else:
			if self.dogList[0].getAdded() < self.catList[0].getAdded():
				return self.dogList.popleft()
			else:
				return self.catList.popleft()


if __name__ == "__main__":

	d = AnimalShelter()

	d.enqueue('kate','cat')
	d.enqueue('bob','dog')
	d.enqueue('qwerty','dog')
	d.enqueue('tom','cat')

	print(d.dequeueAny().name)
	print(d.dequeueAny().name)
	print(d.dequeueAny().name)
