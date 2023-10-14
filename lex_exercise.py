val = 8


def factorial(num):
    fac = [num]
    fac_num = 1
    while num > 1:
        num = num - 1
        fac.append(num)
    print(fac)
    for x in fac:
        fac_num *= x
    return fac_num


print(factorial(val))

