# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# Solution 1: Brute force counting. Of course did not work.

hundred_cnt = 999 - 100 + 1
and_cnt = 999 - 101 + 1

ltrs_1_to_10 =''.join([
	'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',])
# 90 * 10 times

ltrs10_to_19 = ''.join(['ten', 'eleven', 'twelve'
	, 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
	]	)
# 10 times


tees = ''.join(['twenty'
, 'thirty'
, 'forty'
, 'fifty'
, 'sixty'
, 'seventy'
, 'eighty'
, 'ninety'
])
# 10 * 10 times

ans = \
	len(tees) * 10 * 10 + \
	len(ltrs_1_to_10) * 90 * 10 + \
	len(ltrs10_to_19) * 10 + \
	len('hundred') * hundred_cnt + \
	len('and') * and_cnt

print(ans)



# Alternative solution.
# Source: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p017.py


def compute():
	ans = sum(len(to_english(i)) for i in range(1, 1001))
	return str(ans)


def to_english(n):
	if 0 <= n < 20:
		return ONES[n]
	elif 20 <= n < 100:
		return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()


ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]



print(compute())



# Testing

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def to_english2(n):
	if 0 <= n <= 19:
		return ONES[n]
	elif 20 <= n <= 99 :
		return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else '')
	elif 100 <= n <= 999:
		return ONES[n // 100] + 'hundred' + ('and' + to_english(n % 100) if (n % 100 != 0) else '')
	elif 1000 <= 999999:
		return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n%1000 != 0) else "")
	else:
		raise ValueError()

for i in range(1,102):
	print(to_english2(i))

ans = sum(len(to_english2(i)) for i in range(1,1001))
print(ans)