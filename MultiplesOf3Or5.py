def MultipleSum(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    result = MultipleSum(1000)
    print(result)

# Time Complexitity = O(n)
