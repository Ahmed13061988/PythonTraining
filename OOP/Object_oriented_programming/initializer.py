class Item():
    def __init__(self, name, price, quantity):
        print("I'm created")
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item("Phone", 200, 5)
item2 = Item("Laptop", 1000, 3)

