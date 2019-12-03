

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


start = 1
end = 1000

tot_sum = 0
for i in range(start,end):
    if (i % 3 == 0) or (i % 5 == 0):
        tot_sum = tot_sum + i
        # print(i, tot_sum)

print(tot_sum)

# ans = sum(x for x in range(1,1000) if (x % 3 == 0 or x % 5 == 0))
# print(ans)