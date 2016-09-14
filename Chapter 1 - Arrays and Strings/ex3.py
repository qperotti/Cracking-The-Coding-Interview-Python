'''
Exercise 1.3 - URLifi:

Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the 
end to hold the additional characters, and that you are given 
the "true" length of the string.
'''


def URLify_Pythonic(s):
	return '%20'.join(s.split())


# I Treat the string as a list to make it more difficult.
def URLify(s,lenght):
	s_list = list(s)

	# Count # of spaces until last character 
	count = 0
	for i in range(lenght):
		if s_list[i] == ' ':
			count +=1

	# Calculate the new lenght
	new_lenght = count * 2 + lenght - 1

	for i in range(lenght-1,-1,-1):
		if s_list[i] == ' ':
			s_list[new_lenght] = '0'
			s_list[new_lenght-1] = '2'
			s_list[new_lenght-2] = '%'
			new_lenght -= 3
		else:
			s_list[new_lenght] = s_list[i]
			new_lenght -= 1

	return ''.join(s_list)


if __name__ == "__main__":
	print(URLify('Mr John Smith    ',13))
