class CashRegister:

    def __init__(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[str(item)] = float(price)
        self.total_price = self.total_price + price

    def remove_item(self, item, price):
        del self.total_items[str(item)]
        self.total_price = self.total_price - price

    def apply_discount(self, price, discount):
        self.discount = self.total_price + (price * discount)

    def get_total(self):
        return self.total_price - self.discount

    def show_items(self):
        return self.total_items

    def reset_register(self):
        self.total_items = 0
        self.total_price = 0.0


transaction_1 = CashRegister()

CashRegister.add_item(transaction_1, 'oranges', 1.50)
CashRegister.add_item(transaction_1, 'bananas', 1.75)
CashRegister.add_item(transaction_1, 'apples', 1.25)
CashRegister.remove_item(transaction_1, 'bananas', 1.75)

CashRegister.get_total(transaction_1)
CashRegister.show_items(transaction_1)

print('Total Items in basket:', transaction_1.total_items)
print('Total cost of basket', transaction_1.total_price)