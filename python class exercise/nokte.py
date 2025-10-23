from random import random , choice
# # first_name=input("Enter your first name: ")
# # last_name=input("Enter your last name: ")
# #
# # print(f"your name is {first_name} \n your last name is {last_name}")
#
# x = input("enter a :")
# print(f"last chr is {x.split()[-1]}")


# 1404/05/13
# string formating
# str = "hello guys, I am a programming learner."
# print(str.title())

# index = len(str)//2

# print(str[:index])
# print(str[index:])

# str = "madam"

# print(str== str[::-1])

# str = 'abc'
# l = len(str)
# print(str[0]*l+str[1]*l+str[2]*l)

# str='aaabbbcc'
# s1 = str[0]+str[3] + str[6]
# print(s1)

# str = 'Python Programming'

# 'gython ProgramminP'

# a = 2
# b = 3
# a,b = b,a
# s = str[0]
# f = str[-1]
# str = f+str[1:-1]+s
# print(str)

# triditional string formating, .format, fstring

# %
# x = 1.256
# y = 8
# print('x:',x,'\ny:',y)

# print(x, '+',y,'=',x+y)
# print('%f + %i = %f' %(x,y,x+y))

# %[(key)][flag][w][.p]type

# print("%i" %("25"))
# print("%d" %(75))
# print("%i"%(12.52541257854125888))
# print('%c'%(125))
# print("%r" %("python"))

# x = 12257784184455000000000000000000000
# print("%X"%(x))
# print("%E"%(x))


# # print("%ib"%(2))

# d = {'a':'python', '2':'C#', '3':12}

# print("%(3)s"%(d))


# x = float(input("Enter x:"))
# w = int(input("Enter w:"))
# p = int(input("Enter p:"))
# print('%*.3f'%(w,x))

# x = 5
# y = 2.358
# z = 'poiuytreewq'

# print('x: {}\ny:{}'.format(5874,x,z))

# "{" [field_name]["!"conversion][:format_spec]"}"  .format()

# x = 1.454

# print('x is {0:.1}'.format(x))

# format_spec --> [[fill]align][sign][z][#][0][width][grouping_option][.precision][type]
# x = 45.2325

# print('x is {0:^40.3}-'.format(x))


# x = 25
# y = 45.28
# z = 'python'
# # b = input("Enter b")
# print(f"x = {{{{{x}}}}} , y = {y:^8.3f} , z = {z!r}")

# first_name = input("Enter your first name:")
# last_name = input("Enter your last name:")


# print(f"Your name is {first_name}\n"
#       f"Your family is {last_name}")

# print(f"Your name is {first_name}",' '*80
#       f"Your family is {last_name}")

# def add(a,b):
#     return a+b

# print(f"{add(5,3)}")

# import datetime


# my_date = datetime.datetime.today()
# print(f"{my_date:%Y},{my_date:%b},{my_date:%A}")

# sentence = input("Enter  sentence with more than 2 words: ")
# print(f"{sentence.split()[-1]}")

# sentence = sentence.rstrip()
# print(f"{sentence[sentence.rfind(" ")+1:]}")
# sentence = sentence.replace(" ","")
# print(f"{sentence.replace(" ","").replace("\t","")}")


# x = int(input("enter number"))
# if (x%2 == 0) :
#     print("yes")
# else :
#     print("no")


# x = input("please enter your number: ")
# y = input("please enter your number: ")
# if  x.isdigit() and y.isdigit()   :

# else :
#     print(y)


# x = input("please enter your chr: ")
# if x.isalpha() == False:
#     print("enter a chr")
# else :
#     x is  =

# x = input("please enter your height: ")
# y= input ("please enter your weight: ")
# bmi = y/(x**2)

# if bmi < 18.5 :
#     print("underweight")
# elif bmi >= 18.5 and bmi <= 24.9 :
#     print("normal")
# elif bmi >= 25 and bmi <= 29.9 :
#     print("overweight")
# else :
#     print("obese")

# month of date
# x = input("enter your todaydate YYYY-MM-DD :")
# y = x.split("-")
# m = lsty[1]

# x = float(input("enter your angle :"))
# y = float(input("enter your angle :"))
# w = float(input("enter your angle :"))
# if x+y+w == 180 :
#     print("yes")
# else :
#     print("no")

# counter = 0
# s= []
# while counter<3 :
#     n = int(input("enter your number : "))
#     s.append(n)
#     counter +=1

# print(max(s))
# print(s.index(max(s))+1)

# x = int(input("enter your number : "))
# s = 1
# counter = []
# while x == s :
#     if x%s == 0 :
#         counter.append(s)
#     s +=1

# print(counter)

# x = 10
# while x<100 :
#     print (x)
#     x+=2


# price_list = [7, 9, 2 , 10 , 1,7,5]
# d = max(price_list)
# e = price_list.index(d)
# v = price_list[:e+1]
# m =(min(v))
# print(d-m)


# x = input("enter your  number : ")


# count = 100
# while count <= 0:
#     j = 0
#     while count < 10:
#         print(count, end=" ")
#         count -= 1
#         j += 1





# tas = ["1","2","3" , "4" , "5" , "6"]
# n1 = 0
# n2 = 0
# n3 = 0
# n4 = 0
# n5 = 0
# n6 = 0
# n = 100 
# for _ in range(n):
#     x = choice(tas)
#     if x == "1" :
#         n1 +=1
#     elif x== "2" :
#         n2 +=1
#     elif x== "3" :
#         n3 +=1
#     elif x== "4" :
#         n4 +=1
#     elif x == "5" :
#         n5 +=1
#     else :
#         n6 +=1
# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)
# print(n6)


# x = int(input("enter your num1 : "))
# y = int(input("enter your num2 : "))
# if x>y :
#     for i in range(y , x+1) :
#         print(i , end=(" "))
# else :
#       for i in range(x , y+1) :
#         print(i , end=(" "))


# x = input("enter your str : ")
# y = ""
# for i in x :
#     p = ord(i)+3
#     y += chr(p)
# print(y)



# x = [1,2,3,4,5,6,7]
# def f(x):
#     p = max(x)
#     return p

# print(f(x))

# s=[]
# for i in range(5):
#     x= int(input("enter your number : "))
#     s.append(x)

# def u(s):
#     p = max(s)
#     return p

# print(u(s))

# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f

# print(fact(5))


# def numbers(a,b) : 
#     count = 0
#     for char in str(a):
#         if char == str(b):
#             count +=1
#     return count










# def char(*f):
#     x = []
#     y = x.append(q,q2,q3,q4)
#     max = max((y))
#     p = x.index(max)
#     return p

# q = int(input("enter num1: "))
# q2 = int(input("enter num2: "))
# q3 = int(input("enter num3: "))
# q4 = int(input("enter num4: ")) 
# print(char(q,q2,q3,q4))

# def lst(num):
#     dub = 1
#     for i in num:
#         dub = dub*i
#     return(dub)

# num = [2,2,2,2,2]
# p = lst(num)
# print(p)
 

# def inner():
#     print("*" *40)
#     out()
#     print("*" * 40)





# def out():
#     print("hello")



# inner()



# def star(func):
#     def inner(*x , **y):
#         print("*" * 80 , end= "\n")
#         f = func(*x , **y)
#         print (f , end= "\n")
#         print("*" * 80)
#         return "" 
#     return inner

# @star
# def out(name):
#     return f"hello {name}"

# out('mmd')



# def func(start , stop , step = 1):
#     start
#     while start < stop :
#         yield start
#         start += step
# g = func(1 , 100 , 1)
# print(list(g))
        
        
#والروس    
# if (n := int(input("n? "))) > 0:
#     print("Positive:", n)


# s = 'hello'
# # s[0] = 'H'  # ❌ TypeError!

# # راه حل:
# s = 'H' + s[1:]
# print(s)      # 'Hello'
# print(id(s))  # آدرس جدید! 🔄

        
        









