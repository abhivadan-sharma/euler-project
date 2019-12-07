

def gcd(n1, n2):
    ans = 1
    n1, n2 = min(n1, n2), max(n1, n2)
    while n1 > 1:
        i = 2
        while i <= n1:
            if n1 % i == 0 and n2 % i == 0:
                common_factor = i
                i = n1 + 1
                n1 = n1 / common_factor
                n2 = n2 / common_factor
                ans = ans * common_factor
            else:
                i = i + 1
                if i > n1: # If no common factor found
                    n1 = 1
    return ans


gcd(100, 200)
gcd(2, 5)
gcd(1, 100)
gcd(2, 500)
gcd(25, 125)
gcd(125, 625)
gcd(125, 100)
gcd(125, 80)

n1 = 5
n2 = 6
n1, n2 = min(n1, n2), max(n1, n2)
k = 0
k_max = 1000
while (n1 > 1) and (k <= k_max) :
    i = 2
    print("Step 1", "n1 = ", n1, "n2 = ", n2)
    while (i <= n1) and (k <= k_max):
        print("Step 2", "i = ", i,  "n1 = ", n1, "n2 = ", n2)
        if (n1 % i == 0) and (n2 % i == 0):
            common_factor = i
            i = n1 + 1
            n1 = n1 / common_factor
            n2 = n2 / common_factor
            print("\nStep 3a", "Factor = ", common_factor, "i = ", i, "n1 = ", n1, "n2 = ", n2, "\n")
            k = k + 1
        else:
            i = i + 1
            k = k + 1
            print("Step 3b", "i = ", i, "n1 = ", n1, "n2 = ", n2)
            if i > n1:
                n1 = 1
                print("Step 4", "i = ", i, "n1 = ", n1, "n2 = ", n2)
