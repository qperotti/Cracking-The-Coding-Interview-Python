'''
Exercise 8.9 - Parens:

Implement an algorithm to print all valid combinations of n pairs pf parentheses.
'''

def addParen(result, left, right, current, count):

	if left < 0 or right < left:
		return

	if left == 0 and right == 0:
		result.append(current)
	else:

		if left > 0:
			current[count] = '('
			addParen(result,left-1,right,current[:],count+1)

		if right > left:
			current[count] = ')'
			addParen(result,left,right-1,current[:],count+1)


def generateParens(n):
	result = []
	current = [None for _ in range(n*2)]
	addParen(result, n, n, current, 0)
	return [ ''.join(s) for s in result ]


if __name__ == '__main__':

	print(generateParens(3))
