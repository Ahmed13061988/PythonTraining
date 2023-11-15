def strong_number(num):
    number_list = [int(n) for n in str(num)]
    sum_number = 0
    for digit in number_list:
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_number += fact
    print(sum_number)
    if sum_number == num:
        print(True)
    else:
        print(False)


strong_number(40585)
