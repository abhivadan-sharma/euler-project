# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math


def check_prime(n):
	if n == 2 or n == 3:
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3,int(math.sqrt(n))+1,2):
			if n % i == 0:
				return False
		return True


for i in range(2,20):
	print(i, check_prime(i))


ans = 2
i = 3
while i < 2000000:
	if check_prime(i):
		ans = ans + i
	i = i + 2
print(ans)



