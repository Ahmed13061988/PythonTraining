# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = do nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":  # if you don't type in anything it will ask for that input
#         break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue  # this will just skip the iteration (means start the iteration again)
    print(i, end="")
