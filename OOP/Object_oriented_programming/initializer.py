class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity: int = 0):
        # checking if the passed arguments are valid
        assert price > 0, f"Price {price} is not greater than zer0!"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


item1 = Item("Phone", 200, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.pay_rate)
