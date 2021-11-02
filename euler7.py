"""Finds and prints the Nth prime number"""

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def findPrime(x):
    primes = []
    num = 2
    while len(primes) < x:
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes[-1]





if __name__ == '__main__':
    input = int(input("Please enter a positive integer\n"))
    print("The {} prime number is {}".format(input, findPrime(input)))
