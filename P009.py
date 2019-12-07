# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def check_pythagor(n1, n2, n3):
	nums = [n1, n2, n3]
	nums.sort()
	# print (nums)
	if (nums[2] * nums[2]) == (nums[1] * nums[1]) + (nums[0] * nums[0]):
		return True
	else:
		return False

check_pythagor(1,2,3)
check_pythagor(3,2,1)
check_pythagor(4,3,5)

n = 1000
a = 1
while a < n:
	b = a
	while b < n-a:
		# print(a, b, n - a - b)
		b = b + 1
		if check_pythagor(a, b, n-a-b):
			ans = a * b * (n-a-b)
			a = n
			b = n
	a = a + 1

print(ans)
