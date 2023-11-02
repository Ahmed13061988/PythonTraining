def find_common(msg1, msg2):
    new_str = ""
    for i in msg1:
        if i != " ":
            for j in msg2:
                if i == j and i not in new_str:
                    new_str += i
    print(new_str)


find_common("I like Python", "Java is a very popular language")
