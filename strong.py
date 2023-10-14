def strong(num):
    str_num = str(num)
    list1 = list(str_num)
    fac = 1
    result = 0
    for x in list1:
        for i in range(1, int(x) + 1):
            fac *= i
            print(i, "i")
            print(fac, "fac")
            result += fac
    print(result, "result")


strong(145)
