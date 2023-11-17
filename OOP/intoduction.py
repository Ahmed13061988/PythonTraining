class Mobile:
    def __init__(self, brand, price):
        print("From the constructor")
        self.brand = brand
        self.price = price

    def __del__(self):
        print("object has been deleted")

    def purchace(self):
        print(f"Please pay ${mob1.price} at the cashier register")


mob1 = Mobile("Apple", 1119)
mob1.purchace()
mob2 = Mobile("Samsung", 1200)
print(mob1.price, mob2.brand)
