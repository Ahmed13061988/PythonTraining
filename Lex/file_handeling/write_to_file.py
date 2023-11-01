data = open("data.txt", 'r')

print("Before writing to the file, only read")
for line in data:
    print(line)
data.close()

print("After writing to the file, write method")

data2 = open("data.txt", 'w')
num = data2.write("Marge, is Lisa at camp Grenada?")
data2.close()

print("Final sentence")
data3 = open("data.txt", 'r')
for ln in data3:
    print(ln)
