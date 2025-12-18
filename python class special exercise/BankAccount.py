import random
class BankAccount:
    # ۱. فقط نام و موجودی اولیه رو از کاربر می‌گیریم
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name

        # ۲. شماره حساب رو همینجا رندوم تولید و ذخیره می‌کنیم
        self.__account_number = self.__generate_account_number()

        # ۳. موجودی مخفی رو برابر با موجودی اولیه قرار می‌دیم
        self.__balance = initial_balance

    # این متد فقط داخل کلاس صدا زده می‌شه
    def __generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"مبلغ {amount} واریز شد.")
        else:
            print("مبلغ نامعتبر است.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"مبلغ {amount} برداشت شد.")
        else:
            print("موجودی کافی نیست یا عدد اشتباه است.")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Owner: {self.owner_name}")
        # اینجا از خودِ متغیر مخفی استفاده می‌کنیم چون داخل کلاس هستیم
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")


# --- حالا ببین چقدر راحت ساخته می‌شه ---
# کاربر فقط اسم و پولش رو میده، سیستم بقیه کارها رو میکنه
my_acc = BankAccount("Ali", 5000)
my_acc.display_info()
