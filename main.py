from random import choice


class Inventory:
    total_item = 0

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_item += quantity

    def show_product_details(self):
        print("\n---- Product Details ----")
        print(f"Product name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_item -= amount
            print(f"{amount} {self.product_name} has been sold.")
        else:
            print("Insufficient quantity")

    @staticmethod
    def calculate_discount(price, discount_percentage):
        return  price * (1 - discount_percentage / 100)

    @classmethod
    def total_item_report(cls):
        print(f"\nTotal item: {cls.total_item}")

products = []

def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    product = Inventory(product_name, price, quantity)
    products.append(product)
    print(f"{quantity} {product_name} added to inventory.")

def view_product():
    print("\n---- Inventory ----")
    if not products:
        print("Inventory is empty")
    else:
        for product in products:
            product.show_product_details()

def sell_product():
    product_name = input("Enter product name to sell: ").strip()
    for product in products:
        if product.product_name == product_name:
            amount = int(input("Enter amount to sell: "))
            product.sell_product(amount)
            break
        else:
            print("Product not found in inventory.")

def discount_price():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    discounted_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"Discount Price {discounted_price}")

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Sell Product")
    print("4. Calculate Discount")
    print("5. Total Items Report")
    print("6. Exit")

    choice = input("Enter your choice(1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_product()
    elif choice == "3":
        sell_product()
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_item_report()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")