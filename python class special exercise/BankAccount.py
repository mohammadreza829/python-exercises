import random
class BankAccount:
    def __init__(self , owner_name , initial_balance , __account_number , __balance):
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.__account_number = __account_number
        self.__balance = __balance
    
    def __generate_account_number(self):
        return random.randint(1000000000 , 9999999999)
    
    def deposit(self , amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("Amount must be greater than 0")
    def withdraw(self , amount):
        if amount > self.__balance :
            print("Insufficient balance")
        elif amount < 0:
            print("Amount must be greater than 0")
        else:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    def display_info(self):
        print(f"Owner Name: {self.owner_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")
    
    