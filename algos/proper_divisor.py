def proper_divisor(num):
    result = []

    for i in range(1, num):
        if num % i == 0:
            result.append(i)

    return result


print(proper_divisor(220))
