temp = int(input("What is the temperature outside>: "))

if not(temp > 0 and temp <= 30):
    print("The temperature is good today!")
    print("Go outside!")
elif not(temp < 0 or temp > 30):
    print("Stay home, it's bad weather")

