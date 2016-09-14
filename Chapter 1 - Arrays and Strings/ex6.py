'''
Exercise 1.6 - String Compression:

Implement a method to perform basic string compression using the 
counts of repeated characters. For exmaple, the string aabcccccaaa 
would become a2b1c5a3. If the "compressed" string would not become 
smaller than the original string, your method should return the original 
string. You can assume the string has only uppercase and lowercase letters (a-z).
'''


def compress(s):

	strCmp = list()

	count = 1
	for i in range(1,len(s)):
		if s[i] != s[i-1]:
			strCmp.append(s[i-1] + str(count))
			count = 0
		count += 1

	# last repeated characters
	strCmp.append(s[i-1] + str(count))

	return ''.join(strCmp)


def stringCompression(s):

	if len(s) <= 1:
		return s

	# count number of differents consecutive characters
	count = 1
	for i in range(1,len(s)):
		if s[i-1] != s[i]:
			count += 1

	# check if compressed string would be smaller
	if len(s) <= count*2:
		return s

	return compress(s)

if __name__ == "__main__":

	# Test
	print(stringCompression('aabcccccaaa'))
	print(stringCompression('abcde'))
	print(stringCompression('aabbccdd'))
	print(stringCompression('abbbbbbbbd'))
