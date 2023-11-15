def encode(string):
    encode_string = ""
    for i in range(0, len(string)):
        if string[i] in string and string[i] != " ":
            if string[i] not in encode_string:
                counting = string.count(string[i])
                encode_string += f"{counting}{string[i]}"
    print(encode_string)


encode("AAAABBBBCCCCCCCC")
