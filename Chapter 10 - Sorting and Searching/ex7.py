from bitarray import bitarray


def misssingInt(numberList):
	b = bitarray(4000000000)
	a.setall(False)
	for number in numberList:
		b[number] = True

	for i in range(len(b)):
		if b[i] == False:
			return i

