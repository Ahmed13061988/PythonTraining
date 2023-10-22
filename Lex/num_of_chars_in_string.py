def find_num_of_chars(string):
    count = 0
    for i in string:
        if i != " ":
            count += 1
    print(count)


find_num_of_chars("mama")
