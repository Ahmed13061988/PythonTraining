def num_of_words(sentence):
    count = 0
    lst = sentence.split(" ")
    print(lst)
    for i in range(len(lst)):
        count += 1
    print(count)


num_of_words("hello there mama, I miss you!")
