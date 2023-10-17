my_set = {"Ahmed", "Mathieu", "Basim"}

print(my_set, "Before any update")

poped_item = my_set.pop() # removes the first element

print(poped_item)

print(my_set, "After pop()")

my_set1 = {"Rami", "Ahmed", "Atyaf"}
my_set2 = {"Salwa", "Hassan", "Muhammed", "Hussein"}

my_family = my_set1.union(my_set2)
print(my_family)
