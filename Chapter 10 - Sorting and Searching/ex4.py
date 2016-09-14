
def findLength(myList,target):
	index = 1
	while myList[index-1] != -1 and myList[index-1] <= target:
		index *= 2
	return index-1


def tweakBS(myList,target,start,end):
	
	while start <= end:
		middle = (start + end)//2
		if myList[middle] == target:
			return middle

		if target < myList[middle] or myList[middle] == -1:
			end = middle-1
		else:
			start = middle+1

	return -1


def sortedSearch_noSize(myList,target):
	length = findLength(myList,target)
	return tweakBS(myList,target,0,length)




myList = [1,2,4,5,6,10,23,25,100,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
print(sortedSearch_noSize(myList,100))