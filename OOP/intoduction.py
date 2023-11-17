class Mobile:
    def __init__(self, brand, price):
        print("From the constructor")
        self.brand = brand
        self.price = price


mob1 = Mobile("Apple", 1119)
mob2 = Mobile("Samsung", 1200)

print(mob1.price, mob2)
