def sum_square_difference(n):
    sum = n*(n + 1)/2
    sum_of_squares = (((2*n) + 1)*(n + 1)*n)/6
    print(sum_of_squares, sum**2)
    return((sum**2) - sum_of_squares)


if __name__ == '__main__':
    n = 100
    result = sum_square_difference(n)
    print(result)
