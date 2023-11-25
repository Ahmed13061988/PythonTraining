class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount
    def get_walet_balance(self):
        return self.__wallet_balance


c1 = Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(500)
print(c1.get_walet_balance())
