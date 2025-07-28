
from datetime import datetime
import csv



class Inventory:
    total_item = 0

    def __init__(self, product_name, price, quantity, product_expiration_date):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.product_expiration_date = product_expiration_date
        Inventory.total_item += quantity

    def show_product_details(self):
        print("\n---- Product Details ----")
        print(f"Product name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Expiration Date: {self.product_expiration_date}")

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
CSV_FILE = 'data.csv'

def load_products_csv(file):
    with open(file, 'r', newline='') as fl:
        reader = csv.reader(fl)
        next(reader)
        for row in reader:
            if row:
                product_name = row[0]
                price = float(row[1])
                quantile = int(row[2])
                product_expiration_date = row[3]
                product = Inventory(product_name,
                                    price,
                                    quantile,
                                    product_expiration_date)
                products.append(product)

def csv_save(file):
    with open(file, 'w', newline='') as fl:
        writer = csv.writer(fl)
        writer.writerow(['Product name', 'Price', 'Quantity', 'Expiration Date'])
        for item_data in products:
            writer.writerow([item_data.product_name,
                             item_data.price,
                             item_data.quantity,
                             item_data.product_expiration_date])

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            return date_obj.strftime("%d/%m/%Y")
        except ValueError:
            print("Please enter the date in DD/MM/YYYY format: ")

def add_product():
    product_perishable_check = input("Can the product perishable: (Y/N)").strip()
    if product_perishable_check.lower() == "y":
        product_expiration_date = get_date_input("The product expiration date (DD/MM/YYYY):")
    elif product_perishable_check.lower() == "n":
        product_expiration_date = "N/A"
    else:
        print("Invalid input. Please enter Y or N.")
        return

    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    product = Inventory(product_name, price, quantity, product_expiration_date)
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

load_products_csv(CSV_FILE)
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
        csv_save(CSV_FILE)
    elif choice == "2":
        view_product()
    elif choice == "3":
        sell_product()
        csv_save(CSV_FILE)
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_item_report()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")