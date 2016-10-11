'''
Exercise 8.1 - Triple Step:

A child is running up staircase with n steps and can hop either 
1 step, 2 steps, or 3 steps at a time. Implement a method to count 
how many possible ways the child can run up the stairs.
'''


def countWaysRec(n, memo):
	if n < 0: 
		return 0
	elif n == 0:
		return 1
	elif memo[n] != -1:
		return memo[n]
	else:
		memo[n] = countWaysRec(n-1,memo) + countWaysRec(n-2,memo) + countWaysRec(n-3,memo) 
		return memo[n]

def countWays(n):
	memo = [ -1 for _  in range(n+1)]
	return countWaysRec(n, memo)


if __name__ == '__main__':

	print(countWays(3))
	print(countWays(5))