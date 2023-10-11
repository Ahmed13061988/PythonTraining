def find_square(n):
    return n * n


square = find_square(4)


def find_sum(n):
    sum_of_number = n
    while n > 0:
        n -= 1
        sum_of_number += n
    return sum_of_number


sum_1 = find_sum(5)


def change_number(num):
    num += 10


def change_list(num_list):
    num_list.append(20)


num_val = 10
print("*********effect of pass by value*********")
print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)
print("-----------------------------------------------")
val_list = [5, 10, 15]
print("*********effect of pass by reference*********")
print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)
