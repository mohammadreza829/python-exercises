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

    def get_account_number(self):
        return self.__account_number

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


class BankSystem:
    def __init__(self):
        self.accounts = {}  # دیکشنری برای ذخیره: {account_number: account_object}

    def add_account(self, name, initial_balance):
        new_account = BankAccount(name, initial_balance)
        # گرفتن شماره حساب از شیء ساخته شده
        acc_num = new_account.get_account_number()
        # ذخیره در دیکشنری با کلیدِ شماره حساب
        self.accounts[acc_num] = new_account
        print(f"Account created for {name}. Your Account Number is: {acc_num}")
        return acc_num  # شماره رو برمی‌گردانیم تا کاربر بدونه چیه

    def find_account(self, acc_num):
        # جستجو بر اساس شماره حساب
        if acc_num in self.accounts:
            return self.accounts[acc_num]
        else:
            print("Account not found!")
            return None

    def find_by_name(self, name):
        # این حلقه میره توی تک تک اشیاء حساب که ذخیره کردی می‌گرده
        for account in self.accounts.values():
            if account.owner_name == name:
                return account  # اگه پیدا کرد، کلِ شیء حساب رو برمی‌گردونه
        print("No account found with this name.")
        return None


if __name__ == "__main__":
    bank_system = BankSystem()

    test_users = [
        ("Alice", 10000),
        ("Bob", 2000),
        ("Charlie", 500),
        ("David", 0),
        ("Eve", 50000),
    ]

    print("--- Automatically Registering Users ---")
    for name, balance in test_users:
        bank_system.add_account(name, balance)


