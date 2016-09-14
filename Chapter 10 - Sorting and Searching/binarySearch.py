
def search(myList,start,end, target):

	if start > end:
		return -1

	middle = (start+end)//2

	if myList[middle] == target:
		return middle
	if myList[middle] < target:
		return search(myList,middle+1,end,target)
	else:
		return search(myList,start,middle-1,target)


def binarySearch(myList, target):

	return search(myList,0,len(myList)-1,target)


a = [1]

print(binarySearch(a,0))
