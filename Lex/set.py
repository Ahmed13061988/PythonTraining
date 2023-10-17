my_set = {"Ahmed", "Mathieu", "Basim"}

print(my_set, "Before any update")

poped_item = my_set.pop()  # removes the first element

print(poped_item)

print(my_set, "After pop()")

my_set1 = {"Rami", "Ahmed", "Atyaf"}
my_set2 = {"Salwa", "Hassan", "Muhammed", "Hussein"}

my_family = my_set1.union(my_set2)
print(my_family)

my_set4 = {1, 2, 3, 4, 5}
my_set5 = {2, 5, 4, 3, 7}

common_set = my_set4.intersection(my_set5)
print(common_set)

different = my_set4.difference(my_set5)
print(different)

symmetric_difference = my_set4.symmetric_difference(my_set5)

print(symmetric_difference)

