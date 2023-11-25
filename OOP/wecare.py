class Wecare():
    def __init__(self, v_id, v_type, cost, premium=0):
        self.v_id = 0
        self.v_type = v_type
        self.cost = cost

    def v_premium(self, percent, cost):
        self.premium = cost - (cost * percent) / 100
        print(f"The premium is ${self.premium}")


car1 = Wecare("Volvo", 70000)
