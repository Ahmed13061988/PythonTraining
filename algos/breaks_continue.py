# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = do nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":  # if you don't type in anything it will ask for that input
#         break

phone_number = "123-456-789"

# for i in phone_number:
#     if i == "-":
#         continue  # this will just skip the iteration (means start the iteration again)
#     print(i, end="")
for i in range(1, 21):
    if i == 13:
        pass # this will do nothing
    else:
        print(i)


for num in 23, 45, 50, 65, 76, 90:
    if(num%5!=0):
        continue
    if(num%10==0):
        print(num, end=" ")
        continue
    if(num%3==0):
        print(num, end=" ")
