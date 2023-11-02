def prime(lst):
    just_list = []
    prime_numbers = []
    for number in lst:
        for i in range(2, number):
            if number % i == 0:
                just_list.append(number)
    for i in lst:
        if i not in just_list:
            prime_numbers.append(i)
    print(prime_numbers)


prime([7, 9, 11, 13, 15, 20, 23, 24, 26, 30])
