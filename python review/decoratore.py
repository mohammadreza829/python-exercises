# def func():
#     print("hello")
    
    
# def dec(func):
#     def inner():
#         print("start")
#         func()
#         print("end")
#     return inner
    
# func = dec(func)
# func()



def dec(func):
    def inn(x,y):
        if y ==0 :
            return "error : division by zero"
        else :
            return func(x,y)
    return inn
@dec
def div(x,y):
    return x/y
x = int(input("Enter  x number : "))
y = int(input("Enter  y number : "))
print(div(x,y))