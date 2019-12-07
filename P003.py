# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Solution 1 - C Style. Brute Force

import math


def get_all_factors(n):
    # This needs to change. it does not capture all factors
    all_factors = []
    fact_max = int(math.sqrt(n))
    for i in range(1, fact_max + 1):
        if n % i == 0:
            all_factors.append(i)
    return all_factors


def get_prime_factors(n):
    all_factors = get_all_factors(n)
    prime_factors = []
    for factor in all_factors:
        factors_of_factors = get_all_factors(factor)
        # print(factor, factors_of_factors)
        if len(factors_of_factors) == 1:
            prime_factors.append(factor)
    return prime_factors


# all_factors = get_all_factors(100)
# all_prime_factors = get_prime_factors(100)


all_prime_factors = get_prime_factors(600851475143)
ans = max(all_prime_factors)
print(ans)


# Solution 2 - Mathematically driven
# Source: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p003.py
# It does not give unique factors, they may be repeated.


def smallest_prime_factor(n):
    assert n >= 2
    fact_max = int(math.sqrt(n)) + 1
    for i in range(2, fact_max):
        if n % i == 0:
            return (i)  # return i when factor found, and exit the function
    return (n)  # No factor found, which means the number is prime itself


def get_prime_factors(n):
    all_prime_factors = []
    factor = 1
    while factor < n:
        factor = smallest_prime_factor(n)
        all_prime_factors.append(factor)
        n = n / factor
        print(factor, n)
    return (all_prime_factors)


smallest_prime_factor(600851475143)
get_prime_factors(600851475143)





