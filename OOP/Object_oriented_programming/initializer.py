class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # checking if the passed arguments are valid
        assert price > 0, f"Price {price} is not greater than zer0!"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total(self):
        return self.price * self.quantity

    def applying_discount(self):
        return self.price * Item.pay_rate  # Class attribute access

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


item1 = Item("Phone", 200, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

