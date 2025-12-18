from Bank import BankAccount

# ابتدا یک حساب می‌سازیم
name = input("نام خود را وارد کنید: ")
money = float(input("موجودی اولیه را وارد کنید: "))
user_account = BankAccount(name, money)

while True:
    print("\n--- منوی بانک ---")
    print("1. نمایش اطلاعات حساب")
    print("2. واریز پول")
    print("3. برداشت پول")
    print("4. نمایش موجودی")
    print("5. خروج")
    
    choice = input("یک گزینه انتخاب کنید: ")

    if choice == "1":
        user_account.display_info()
    
    elif choice == "2":
        amount = float(input("مبلغ واریز: "))
        user_account.deposit(amount)
    
    elif choice == "3":
        amount = float(input("مبلغ برداشت: "))
        user_account.withdraw(amount)
    
    elif choice == "4":
        print(f"موجودی فعلی: {user_account.get_balance()}")
    
    elif choice == "5":
        print("با تشکر از اعتماد شما. خروج...")
        break
    
    else:
        print("گزینه اشتباه است!")