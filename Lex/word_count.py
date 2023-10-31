def word_count(sentence):
    output = {}
    array = sentence.split(" ")
    count = 0
    for i in range(len(array)):
        for j in range(len(array) - 1, -1, -1):
            if len(array[i]) == len(array[j]):
                count += 1
        output[array[i]] = count
    print(output)


word_count('I love python and it so easy to learn')
