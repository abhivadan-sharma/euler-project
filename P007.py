# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


import math


def check_prime(n):
	flag = True
	i = 2
	while i <= math.sqrt(n) :
		if n % i == 0 :
			flag = False
			i = n
		i = i + 1
	return flag


check_prime(2)
check_prime(3)
check_prime(5)
check_prime(7)
check_prime(100)
check_prime(121)

cnt = 0
n = 1
while cnt < 10001:
	n = n + 1
	if check_prime(n):
		cnt = cnt + 1
		print(cnt, n)
