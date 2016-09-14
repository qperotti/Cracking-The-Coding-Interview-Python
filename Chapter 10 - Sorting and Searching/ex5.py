

def search(myList,start,end,target):
	if start > end:
		return -1;

	middle = (start + end)//2
	if target == myList[middle]:
		return middle

	if myList[middle] != '':
		if target < myList[middle]:
			return search(myList,start,middle-1,target)
		else:
			return search(myList,middle+1,end,target)
	else:
		before = after = middle
		before, after = before-1, after+1
		while(True):

			# We look backwards
			if before >= start:
				if myList[before] != '':
					if target == myList[before]:
						return before
					if target < myList[before]:
						return search(myList,start,before-1,target)
					# Stop loking backwards
					before = start-1
				else:
					before -= 1

			# We look forwards
			elif after <= end:
				if myList[after] != '':
					if target == myList[after]:
						return after
					if target > myList[after]:
						return search(myList,after+1,end,target)
					# Stop loking forwards
					after = end+1
				else:
					after += 1
			# We arrived to both ends
			else:
				return -1






def sparseSearch(myList, target):
	return search(myList,0,len(myList)-1,target)






myList = ['at','','','','ball','','','car','','','dad','','',]
print(sparseSearch(myList,'ball'))