
def partition(myList, start, end):
	pivot = myList[(start + end)//2]

	while start <= end:

		while myList[start] < pivot:
			start += 1
		while myList[end] > pivot:
			end -= 1

		if start <= end:
			myList[start], myList[end] = myList[end], myList[start]
			start += 1
			end -= 1

	return start

def quickSort(myList, start, end):

	index  = partition(myList,start,end)

	if start < index -1:
		quickSort(myList,start,index-1)
	if index < end:
		quickSort(myList,index,end)


a = [3,2,6,5,7,8,1,10,100,69]

quickSort(a,0,9)
print(a)