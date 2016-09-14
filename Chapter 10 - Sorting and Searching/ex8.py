from bitarray import bitarray


def findDuplicates(numberList):
	b = bitarray(32000)
	a.setall(False)
	for number in numberList:
		if b[number] == True:
			print(number)
		b[number] = True
