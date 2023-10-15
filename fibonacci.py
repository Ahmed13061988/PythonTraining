def fibonacci(n):
    list_1 = [0, 1]
    for i in range(1, n):
        value = list_1[i] + (list_1[i - 1])
        list_1.append(value)
    return list_1


print(fibonacci(11))
