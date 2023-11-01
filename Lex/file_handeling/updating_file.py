data = open("data.txt", "a")

data.write("Hello Father\nHello mother!")
data2 = open("data.txt", 'r')
# print(new_file)  # This will return integer which is number of characters been added to the original text
for line in data2:
    print(line)
