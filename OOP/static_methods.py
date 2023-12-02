class Customer:
    @staticmethod
    def calculate_tax(cust_type):
        if cust_type == 'member':
            return 0.10
        else:
            return 0.20
