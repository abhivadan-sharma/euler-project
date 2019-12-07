# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Hint: 2520 is (2 ** 3) * (3 ** 2) * 5 * 7


# Solution 1: Brute Force, using only the prime numbers in the given list

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


# Solution 2: Using Commutative property of LCM
# Source: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p005.py

def gcd(n1, n2):
	ans = 1
	n1, n2 = min(n1, n2), max(n1, n2)
	while n1 > 1:
		i = 2
		while i <= n1:
			if n1 % i == 0 and n2 % i == 0:
				common_factor = i
				i = n1 + 1
				n1 = n1 / common_factor
				n2 = n2 / common_factor
				ans = ans * common_factor
			else:
				i = i + 1
				if i > n1: # If no common factor found
					n1 = 1
	return ans


curr_gcd = 1
curr_lcm = 1
for i in range(1, 21):
	curr_gcd = gcd(curr_lcm, i)
	curr_lcm = curr_lcm * i / curr_gcd
	print(i, curr_gcd, curr_lcm)

