
def merge(myList, start1, end1, start2, end2):
	tmpList = list()
	index1, index2 = start1, start2

	while(index1 <= end1 and index2 <= end2):
		if myList[index1] < myList[index2]:
			tmpList.append(myList[index1])
			index1 += 1
		else:
			tmpList.append(myList[index2])
			index2 += 1

	while(index1 <= end1):
		tmpList.append(myList[index1])
		index1 += 1

	while(index2 <= end2):
		tmpList.append(myList[index2])
		index2 += 1

	current = start1
	for i in range(len(tmpList)):
		myList[current] = tmpList[i]
		current += 1





def mergeSort(myList, start, end):

	if start < end:
		
		middle = (start + end)//2

		mergeSort(myList,start,middle)
		mergeSort(myList,middle+1,end)
		merge(myList,start,middle,middle+1,end)


a = [3,2,6,5,7,8,1,10,100,69]

mergeSort(a,0,9)
print(a)