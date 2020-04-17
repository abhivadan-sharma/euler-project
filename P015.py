

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?


def factorial(n):
	if n == 0 :
		return 1
	else :
		return n * factorial(n - 1)


def ncr(n, r):
	return factorial(n) / (factorial(r) * factorial(n-r))


factorial(5)
factorial(6)

ans = ncr(40,20)  # We are looking for 2Ncn
print(ans)


def ncr2(n, r):
	r = min(r, n-r)
	ans = 1
	for i in range(0, r):
		ans = ans * (n - i)
	ans = ans / factorial(r)
	return ans

ncr2(4,2)
ans = ncr2(40,20)
print(ans)
