# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def get_all_factors(n):
	n_max = int(math.sqrt(n)) + 1
	factors = []
	for i in range(1, n_max):
		print(i)
		if n % i == 0:
			factors.append(i)
			factors.append(n/i)
	return factors

get_all_factors(20)
