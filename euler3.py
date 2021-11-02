def prime(x):
    if x <= 1:
        return False

    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False

    return True

def largestPrime(x):
    primeFactors = []

    for i in range(2, x//2 + 1):
        if x % i == 0:
            if prime(i):
                primeFactors.append(i)

    return max(primeFactors)

if __name__ == '__main__':
    input = int(input("please enter a positive number\n"))

    print("The largest prime factor of {} is {}".format(input, largestPrime(input)))
