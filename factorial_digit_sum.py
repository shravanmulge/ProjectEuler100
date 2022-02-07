def factorial_digit_sum(n):
    product = 1
    sum = 0
    for i in range(n, 1, -1):
        product = product * i
    product = list(str(product))
    for item in product:
        sum += int(item)
    return sum


if __name__ == '__main__':
    num = 100
    result = factorial_digit_sum(num)
    print(result)
