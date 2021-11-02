"""computes the largest prime factor for a given integer input"""

import sys
factors = dict()
sys.setrecursionlimit(2000)

def prime(x):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def largestPrime(x, fac):
    global factors

    if x in factors:
        ans = factors[x]
    elif prime(x):
        ans = x
    elif x % fac == 0:
        if prime(fac):
            ans = largestPrime(x//fac, fac)
    else:
        ans = largestPrime(x, fac+1)

    if x not in factors:
        factors[x] = ans

    return ans

if __name__ == '__main__':
    input = int(input("please enter a positive number\n"))

    print("The largest prime factor of {} is {}".format(input, largestPrime(input, 2)))
