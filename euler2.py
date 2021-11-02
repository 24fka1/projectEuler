"Computes the sum of the even fibonacci numbers less than the specified value"
def fib(x):
    fib1 = 0
    fib2 = 1
    next = 0
    total = 0

    while (next + fib1 < x) or (next + fib2 < x):
        next = fib1 + fib2
        if fib1 < fib2:
            fib1 = next
        else:
            fib2 = next

        if next % 2 == 0:
            total += next

    return total


if __name__ == '__main__':
    input = int(input("please enter a number and I will print the sum of the even fibonacci numbers less that that number:\n"))
    print("The sum of the even fibonacci numbers less than {} is {}".format(input, fib(input)))
