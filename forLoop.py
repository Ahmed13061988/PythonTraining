import time

for i in range(1, 11):  # regular range loop, the last number is not included.
    print(i, end="")

for i in range(10):  # regular range loop
    print(i + 1, end=" ")

name = "Ahmed"

for i in name:  # looping over string
    print(i, end=",")

for i in range(10, 0, -1):  # looping backwards
    time.sleep(1)
    print(i)
print("Happy new year!")
