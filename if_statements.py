age = int(input("what is your age?: "))

if 18 <= age <= 99:
    print("You are an adult")
elif age <= 0:
    print("You haven't been born yet!")
elif age == 100:
    print("You are 100 years old")
else:
    print("you are a child!")
