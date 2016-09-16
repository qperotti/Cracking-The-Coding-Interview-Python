'''
Exercise 10.11 - Peaks and Valleys:

In an array of integers, a "peak" is an element which is greater
than or equal to the adjacent integers and a "valley" is an element
which is less than or equal to the adjacent integers. Given an array 
of integers, sort the array into an alternating sequence of peaks and valleys.

'''

def sortValleyPeak(nums):


	for i in range(1,len(nums),2):
		makeChanges(nums,i)
	return nums


def makeChanges(nums,index):

	# To avoid out of index
	if index+1 <= len(nums)-1:

		# Is already sorted
		if nums[index-1] < nums[index] and nums[index] > nums[index+1]:
			return

		# If not sorted swap middle element with the largest adjacent
		if nums[index-1] > nums[index+1]:
			nums[index], nums[index-1] = nums[index-1], nums[index]
		else:
			nums[index], nums[index+1] = nums[index+1], nums[index]

	else:
		if nums[index-1] > nums[index]:
			nums[index], nums[index-1] = nums[index-1], nums[index]


if __name__ == "__main__":

	nums = [9,1,0,4,8,7]
	print(sortValleyPeak(nums))