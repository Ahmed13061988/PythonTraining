food = ["pizza", "falafel", "burger", "hotdog", "spaghetti"]

for x in food:
    for i in x:
        if i == "z":
            i = "o"
print(food)
