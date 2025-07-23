# 1. Task: Create a Banking System
# Problem: Design a banking system where users can create accounts, deposit money, withdraw money, and check their balance.
# Details:
# Create a BankAccount class with attributes like account_number, account_holder, and balance.
# Implement methods like deposit(), withdraw(), check_balance(), and transfer().
# Implement a method to check the account’s balance after each transaction.
# Optionally, include a Transaction class to store transaction history.

class BankAccount:
    def __init__(self):
        self.acc_no = {}
        self.acc_balance = {}
        self.user_name = {}
        self.email = {}

    def create_account(self):
        acc_no = int(input("Enter a new account number: "))
        if acc_no not in self.acc_balance:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            self.acc_balance[acc_no] = 0
            self.user_name = name
            self.email = email
            print(f"Account {acc_no} created successfully.")
        else:
            print("Account already exists.")

    def deposit(self):
        acc_no = int(input("Enter your account number: "))
        if acc_no in self.acc_balance:
            amount = int(input("Enter the amount to deposit: "))
            self.acc_balance[acc_no] += amount
            print(f"Deposited {amount}. New balance: {self.acc_balance[acc_no]}")
        else:
            print("Account not found. Please create an account first.")

    def withdraw(self):
        acc_no = int(input("Enter your account number: "))
        if acc_no in self.acc_balance:
            amount = int(input("Enter the amount to withdraw: "))
            if self.acc_balance[acc_no] >= amount:
                self.acc_balance[acc_no] -= amount
                print(f"Withdrew {amount}. Remaining balance: {self.acc_balance[acc_no]}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found. Please create an account first.")

    def checking(self):
        acc_no = int(input("Enter your account number: "))
        if acc_no in self.acc_balance:
            print(f"Account balance: {self.acc_balance[acc_no]}")
            print(f"Account holder: {self.user_name}")
            print(f"Email: {self.email}")
        else:
            print("Account not found. Please create an account first.")
b1 = BankAccount()

while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Account Details")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            b1.create_account()
        elif choice == 2:
            b1.deposit()
        elif choice == 3:
            b1.withdraw()
        elif choice == 4:
            b1.checking()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

