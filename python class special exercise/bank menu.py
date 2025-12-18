from Bank import BankAccount

print("--- Welcome to the Banking System ---")
name = input("Enter your name: ")
initial_money = float(input("Enter initial balance: "))

# ساخت شیء از روی کلاس
user_account = BankAccount(name, initial_money)

while True:
    print("\n========= MENU =========")
    print("1. Account Info")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    print("========================")
    
    choice = input("Please select an option (1-5): ")

    if choice == "1":
        user_account.display_info()
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        user_account.deposit(amount)
    
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        user_account.withdraw(amount)
    
    elif choice == "4":
        print(f"Current Balance: {user_account.get_balance()}")
    
    elif choice == "5":
        print("Thank you for using our system. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")