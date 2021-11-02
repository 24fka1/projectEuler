def sum_of_squares(x):
    sum = 0
    for i in range(x+1):
        sum += (i**2)
    return sum

def square_of_sum(x):
    sum = 0
    for i in range(x+1):
        sum += i
    return sum**2

if __name__ == '__main__':
    input = int(input("please enter a positive number\n"))
    ans = square_of_sum(input) - sum_of_squares(input)
    print("The differnce between the sum of squares and square of the sum is {}".format(ans))
