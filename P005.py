# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Hint: 2520 is (2 ** 3) * (3 ** 2) * 5 * 7


import math


def get_all_factors(n):
	n_max = int(math.sqrt(n)) + 1
	factors = []
	for i in range(1, n_max):
		# print(i)
		if n % i == 0:
			factors.append(i)
			factors.append(n/i)
	return factors

# get_all_factors(20)
# get_all_factors(5)


n = 20
ans = 1
for i in range(2, n+1):
	if len(get_all_factors(i)) == 2: # checks for prime numbers
		highest_power = max(x for x in range(1, n+1) if (i ** x) <= n) # highest power which is less than the given number
		print(i, highest_power)
		ans = ans * i ** highest_power
print(ans)