import random

class BankAccount:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.__account_number = self.__generate_account_number()
        # Ensure initial balance isn't negative
        self.__balance = initial_balance if initial_balance >= 0 else 0

    def __generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited: {amount}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew: {amount}")
        elif amount > self.__balance:
            print("Error: Insufficient balance.")
        else:
            print("Error: Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print("\n--- Account Details ---")
        print(f"Owner: {self.owner_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: {self.__balance}")
        print("-----------------------")

if __name__ == "__main__":
    # Test section - Only runs when bank.py is executed directly
    print("Running Test Mode...")
    my_acc = BankAccount("Ali", 5000)
    my_acc.display_info()
    my_acc.deposit(1000)
    my_acc.withdraw(200)
    print(f"Final Test Balance: {my_acc.get_balance()}")