class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        
    def sell(self , num):
        if self.quantity <= self.price*num:
            print("Not enough stock")
        else:
            self.quantity -= self.price*num
            print("sold successfully")
            print(f"Remaining stock: {self.quantity}")
        