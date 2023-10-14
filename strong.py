def strong(num):
    str_num = str(num)
    list1 = list(str_num)
    fac = []
    result = 0
    for x in list1:
        fac.append(int(x))

    for i in fac:
        while i > 0:
            fact = i
            new_number = i - 1
            final = new_number * (i + 1)
            i -= 1
            result += final
    print(result)


strong(145)
