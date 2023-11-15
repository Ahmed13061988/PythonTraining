def check_amicable_numbers(num1, num2):
    sum1 = 0
    sum2 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            sum1 += i
    for x in range(1, num2):
        if num2 % x == 0:
            sum2 += x
    if sum2 == num1 and sum1 == num2:
        return True
    else:
        return False


print(check_amicable_numbers(220, 284))
