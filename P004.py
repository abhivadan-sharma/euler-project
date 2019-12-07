# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


# Solution 1 - C style

def check_palindrome(n):
	n_str = str(n)
	try_num = int(len(n_str)/2)
	ans = True
	for i in range(0,try_num):
		if n_str[i] != n_str[-1-i]:
			return False
	return ans


# Solution 2 - Python string slicing
def check_palindrome(n):
	n_str = str(n)
	res = n_str == n_str[::-1]
	return res

def largest_palindrome():
	pals = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			n = i * j
			# print(i, j, n, check_palindrome(n))
			if check_palindrome(n):
				pals.append(n)
	return max(pals)


largest_palindrome()





check_palindrome(9009)
check_palindrome(9001)
check_palindrome(9001009)