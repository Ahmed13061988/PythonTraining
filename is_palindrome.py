def is_palindrome(num):
    boolean = True
    backwards = []
    num_str = str(num)
    original = list(num_str)
    for n in range(len(num_str) - 1, -1, -1):
        backwards.append(num_str[n])
    for i in range(len(original) - 1):
        if original[i] != backwards[i]:
            boolean = False
    return boolean


print(is_palindrome(12345))


