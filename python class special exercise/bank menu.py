from Bank import BankAccount, BankSystem

my_bank = BankSystem()

test_users = [("Alice", 10000), ("Bob", 2000)]
for name, bal in test_users:
    my_bank.add_account(name, bal)
    
while True:
    print("\n========= GLOBAL BANK MENU =========")
    print("1. Open New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Search Account (by Name)")
    print("6. Exit")
    print("====================================")

    print("Current users in system:", [acc.owner_name for acc in my_bank.accounts.values()])
    choice = input("Select an option (1-6): ")

    # --- گزینه 1: افتتاح حساب ---
    if choice == "1":
        name = input("Enter owner name: ")
        initial_money = float(input("Enter initial balance: "))
        # متد add_account خودش شیء رو می‌سازه و توی دیکشنری ذخیره می‌کنه
        acc_num = my_bank.add_account(name, initial_money)
        print(f"DONE! Your account number is: {acc_num}")

    # --- گزینه 2: واریز وجه ---
    elif choice == "2":
        acc_num = int(input("Enter your account number: "))
        account = my_bank.find_account(acc_num)  
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("Account not found!")

    # --- گزینه 3: برداشت وجه ---
    elif choice == "3":
        acc_num = int(input("Enter your account number: "))
        account = my_bank.find_account(acc_num)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("Account not found!")

    # --- گزینه 4: انتقال وجه (پیشرفته) ---
    elif choice == "4":
        sender_num = int(input("Enter YOUR account number (Sender): "))
        receiver_num = int(input("Enter RECEIVER account number: "))
        amount = float(input("Enter transfer amount: "))

        # پیدا کردن هر دو حساب
        sender = my_bank.find_account(sender_num)
        receiver = my_bank.find_account(receiver_num)

        if sender and receiver:
            if sender.get_balance() >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("Transfer completed successfully!")
            else:
                print("Transfer failed: Insufficient balance.")
        else:
            print("Error: One or both account numbers are invalid.")

    # --- گزینه 5: جستجو بر اساس نام ---
    elif choice == "5":
        name_to_search = input("Enter name to search: ")
        account = my_bank.find_by_name(name_to_search)
        if account:
            account.display_info()

    # --- گزینه 6: خروج ---
    elif choice == "6":
        print("Thank you for using Global Bank. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
