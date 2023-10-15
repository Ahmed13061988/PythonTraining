val = 0


def factorial(num):
    fac = [num]
    fac_num = 1
    while num > 1:
        num = num - 1
        fac.append(num)
    for x in fac:
        fac_num *= x
    return fac_num



# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
#
#
# factorial()

print(factorial(145))
