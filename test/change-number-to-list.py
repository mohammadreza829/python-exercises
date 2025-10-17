def func(numbers):
    k=0
    for i in numbers:
        if i>0:
            x=i**2
            k+=x
    return k


# my_numbers=[-1,2,-3,4,5]
# result=func(my_numbers)
# print(result)


user_inout=input("Enter your number:")
numbers_str=user_inout.split()
numbers=[int(i) for i in numbers_str]
result=func(numbers)
print(result)
