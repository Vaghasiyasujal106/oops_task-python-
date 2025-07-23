# Task: Build a Simple E-Commerce Shopping Cart
# Problem: Implement a basic shopping cart system where users can add and remove products and calculate the total price.
# Details:
# Create a Product class with attributes like name, price, and quantity.
# Create a Cart class that holds a list of products and has methods like add_product(), remove_product(), and calculate_total().
# Implement a method to check the availability of products before adding them to the cart.

class Products:
    def __init__(self):
        self.productId = [1, 2, 3]
        self.productName = ["Pizza", "Burger", "Sandwich"]
        self.productPrice = [300, 100, 150]
        self.productQty = [10, 15, 25]
        self.cart = {}  # To store items added to the cart

    def show_table(self):
        print("Available Products:")
        for Id, name, price, qty in zip(self.productId, self.productName, self.productPrice, self.productQty):
            print(f"ID: {Id}, {name}: ₹{price}, Quantity Available: {qty}")

    def add_to_cart(self):
        self.show_table()
        prod_id = int(input("Enter the Product ID to add to the cart: "))
        if prod_id in self.productId:
            prod_id -= 1  #for indexing
            qty = int(input("Enter quantity: "))
            if qty > 0 and qty <= self.productQty[prod_id]:
                if prod_id in self.cart:
                    self.cart[prod_id]['qty'] += qty
                else:
                    self.cart[prod_id] = {
                        'name': self.productName[prod_id],
                        'price': self.productPrice[prod_id],
                        'qty': qty,
                    }
                self.productQty[prod_id] -= qty
                print(f"{self.productName[prod_id]} (x{qty}) added to the cart.")
            else:
                print("Invalid quantity. Please try again.")
        else:
            print("Invalid Product ID. Please try again.")
    @property
    def get_total(self):
        total = 0
        for item in self.cart.values():
            item_total = item['price'] * item['qty']
            total += item_total
        return total
    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in self.cart.values():
                item_total = item['price'] * item['qty']
                print(f"{item['name']}: ₹{item['price']} x {item['qty']} = ₹{item_total}")
            total = self.get_total
            print(f"Total: ₹{total}")

    def make_payment(self):
        if not self.cart:
            print("\nYour cart is empty. Add items to the cart before making a payment.")
        else:
            total = self.get_total
            print(f"You have to pay : ₹{total}")
            self.cart.clear()  # Clear the cart after payment
            print("\nProcessing your payment...")
            print("Payment successful! Thank you for your purchase.")

    def shoppingDetails(self):
        while True:
            print("Menu:")
            print("1. Show the table")
            print("2. Add to cart")
            print("3. Show the cart")
            print("4. Make payment")
            print("5. Exit")

            try:
                user = int(input("Enter the number of your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Perform the selected action
            if user == 1:
                self.show_table()
            elif user == 2:
                self.add_to_cart()
            elif user == 3:
                self.show_cart()
            elif user == 4:
                self.make_payment()
            elif user == 5:
                print("Exiting the app. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

items = Products()
items.shoppingDetails()


