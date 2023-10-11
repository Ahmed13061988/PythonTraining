def find_square(n):
    return n * n


square = find_square(4)

print(square)


def find_sum(n):
    sum_of_number = n
    while n > 0:
        n -= 1
        sum_of_number += n
    return sum_of_number


sum_1 = find_sum(5)
print(sum_1)
