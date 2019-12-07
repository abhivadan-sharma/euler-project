


def get_prime_factors(n):
    ans = []
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                factor = i
                ans.append(factor)
                i = n + 1 # End the second loop
                n = n / factor
            else:
                i = i + 1
    return ans


get_prime_factors(600851475143)
get_prime_factors(200)
get_prime_factors(8)
get_prime_factors(5)
