"""Computes the sum of all the multiples of 3 or 5 and prints the sum"""
def mult(x):
    sum = 0
    counter = 0
    while counter < x:
        if (counter % 3 == 0) or (counter % 5 == 0):
            sum += counter
        counter += 1

    print(sum)


if __name__ == '__main__':
    input = int(input("please enter a positive number\n"))
    print("The sum of the multiples of 3 or 5 below {}:".format(input))
    mult(input)
