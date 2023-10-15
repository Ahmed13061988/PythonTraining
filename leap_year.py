# def is_leap(n):
#     leap = [n]
#     for i in range(15):
#         n = n + 4
#         if n % 4 == 0:
#             leap.append(n)
#     return leap

def is_leap(n):
    leap = [n]
    while len(leap) < 15:
        n += 1
        if n % 4 == 0:
            leap.append(n)
    return leap


print(is_leap(2000))
