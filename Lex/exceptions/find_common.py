def find_common(msg1, msg2):
    new_str = ""
    for i in msg1:
        if i != " ":
            for j in msg2:
                if i == j and i not in new_str:
                    new_str += i
                else:
                    new_str = "-1"
    print(new_str)


find_common("Jabbar", "You")
