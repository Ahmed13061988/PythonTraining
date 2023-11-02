def find_pairs_of_numbers(lst, n):
    output = 0
    for i in range(0, len(lst) - 1):
        for j in range(i, len(lst) - 1):
            if lst[i] + lst[j + 1] == n:
                output += 1
    print(output)


find_pairs_of_numbers([3, 4, 1, 8, 5, 9, 0, 6], 9)
