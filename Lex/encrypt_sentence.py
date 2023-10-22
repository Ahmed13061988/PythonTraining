import re


def encrypt_sentence(msg):
    vowels = "aAEeIiUuYyoO"
    new_array = msg.split(" ")
    for i in range(len(new_array)):
        if i % 2 == 0:
            for j in range(len(new_array[i])):
                if new_array[i][j] in vowels:
                    print(new_array[i])
        else:
            new_array[i] = (new_array[i][::-1])
    # print(new_array)


encrypt_sentence("the sun rises in the east")
