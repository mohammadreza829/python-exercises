# def greet(name):              #1
#     print(f"hello {name}")
# sayhi = greet
# sayhi("alice")   


# def add(a,b):         #2
#     return a+b
# mathop = add(3,5)
# print(mathop)

# def multiply(x,y):            #3  important
#     return x*y
# def applyop(nums , op):
#     return op (nums[0] , nums[1])
# nums = [2,3,4,5,6]
# print(applyop(nums , multiply))


# def square(n):      #4
#     return n*n
# calc = square
# print(calc(4))


# def iseven(num):          #5 important
#     if num%2 == 0:
#         return True
# def checkproperty(numbers , prop):
#     result = []
#     for n in numbers:
#         if prop(n):
#             result.append(n)
#     return result
# nums = [1,2,3,4,5,6]
# evens = checkproperty(nums , iseven)
# print(evens)


# def subtract(a,b):          #6
#     return a-b
# difffunc = subtract
# print(difffunc(10,4))


# def power(base , exp):        #14
#     return base**exp
# exponentiate = power
# print(exponentiate(2,3))


# def round_num(n):       #20
#     return round(n)
# approx = round_num
# print(approx(3.7))


# def make_multiplier(factor):        #31
#     def multi(x):
#         return x*factor
#     return multi

# doubler = make_multiplier(3)
# print(doubler(5))
        

# def builder_for_filter(criteria):         #39 important
#     if criteria == "even":
#         def is_even(n):
#             return n % 2 == 0
#         return is_even
#     elif criteria == "odd":
#         def is_odd(n):
#             return n % 2 == 1
#         return is_odd
# filters = {
#     "even" : builder_for_filter("even"),
#     "odd" : builder_for_filter("odd")
# }   
# mynum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# filter_func = filters["even"]
# result = []
# for num in mynum:
#     if filter_func(num):
#         result.append(num)
# print(f"the enven numbers are : {result}")


# def custom_reducer(init , data , reduce_func):          #41 important shakkkkkkkkkkkkkkkkkkkkkkk
#     def add(x,y):
#         return x+y
#     accumulator = init
#     for i in data:
#         accumulator = reduce_func(i , accumulator)
#     return accumulator
# def add(a,b):
#     return a-b
# num = [10,20,30,40,50,60]
# item = custom_reducer(0,num,add)
# print(item)


# def runtim_adder(a):                #61
#     def inner(b):
#         return a+b
#     return inner
# add = runtim_adder(5)
# print(add(3))


# def square(a):            #37
#     return a**2
# def cube(b):
#     return b**3
# def fourth(c):
#     return c**4
# powers = [square , cube , fourth]
# def apply_power(index , n):
#     return powers[index](n)

# print(apply_power(1 , 5))


# def double(a):      #40
#     return a*2
# def add(a):
#     return a+5
# funcs_list = [double , add]
# def chain_calls(start_val , funcs_list):
#     for func in funcs_list:
#         start_val = func(start_val)
#     return start_val

# print(chain_calls(5 , funcs_list))


# def uppercase(a):           #42
#     return a.upper()
# def lowercase(a):
#     return a.lower()
# def titlecase(a):
#     return a.title()
# funcs_list = (uppercase , lowercase , titlecase)
# def apply_sequence(text , funcs_list):
#     for i in funcs_list:
#         text = i(text)
#     return text
# apply = apply_sequence("hello world" , funcs_list)
# print(apply)



# def dynamic_divider(precision):             #43 important shakkkkkk
#     def divider(a,d):
#         result = a/d
#         rounded_result = round(result , precision)
#         return rounded_result
#     return divider
# divide = dynamic_divider(4)
# print(divide(10,3))


# def by_len(s) :                 #58 important 
#     return len(s)
# def sort_by_len(l) :
#     return sorted(l , key = by_len , reverse=True)
# sorted_txt = sort_by_len(["apple" , "banana" , "cherry" , "date" , "elderberry"])
# print(sorted_txt)


# def menu_dispatcher(options_dict):            #44 important
#     def inner(option):
#         return options_dict[option]
#     return inner
# options = {
#     "a" : "apple",
#     "b" : "banana",
#     "c" : "cherry"
# }
# menu = menu_dispatcher(options)
# print(menu("a"))



# def select_apple():                   #44.2 important
#     return "you were selected apple"
# def select_banana():
#     return "you were selected banana"
# def exit_menu():
#     return "exite"
# options_with_functions = {
#     "1": select_apple,
#     "2": select_banana,
#     "q": exit_menu
# } 
# def menu_dispatcher(options_dict):
#     def inner(choice):
#         result = options_dict.get(choice)
#         if result :
#             return result()
#         else : 
#             return "نامعتبر"
#     return inner

# txt = menu_dispatcher(options_with_functions)
# print(txt("1"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# def logger_wrapper(func):       #45 imp
#     def wrapper(*args):
#         print(f"called this func : {func.__name__} ")
#         print(f"with this numbers : {args}")
#         result = func(*args)
#         return result
#     return wrapper
# def add(a,b):
#     return a+b
# logged = logger_wrapper(add)
# print(logged(2,3))


# def partial_applier(func, fixed_arg):       #47
#     def applier(arg):
#         result = func(fixed_arg , arg  )
#         return result
#     return applier
# def add(a,b):
#     return a+b
# partial = partial_applier(add, 10)
# print(partial(5))


# def compose_two(f1, f2):
#     def composed_func(x):
#         return f1(f2(x))
#     return composed_func
# def double(x):
#     return x * 2
# def add_ten(x):
#     return x + 10
# my_func = compose_two(double, add_ten)

# result = my_func(5)  
# print(result) 


# def memoizer(func):             #59 importantttttttttt
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             result = func(*args)
#             cache[args] = result
#             return result
#     return wrapper
# # # fib 1
# # def fib(n):
# #     if n<=2 :
# #         return 1
# #     return fib(n-1) + fib(n-2)

# #fib 2 
# def fib(n):
#     if n<=1 :
#         return n
#     prev1 , prev2 = 0 ,1
#     for i in range(2,n+1):
#         prev1 , prev2 = prev2 , prev1 + prev2
#     return prev2

# memoized_fib = memoizer(fib)
# print(memoized_fib(6))


def stateful_counter():     #68
    counter = 0 
    def count():
        nonlocal counter
        counter +=1
        return counter
    return count

a= stateful_counter()
print(a())
print(a())
print(a())

# def cache_decoy(func):                      #77    shakkkkkkk


# methods = {
#     int: lambda x: f"عدد {x} دریافت شد. مربعش: {x**2}",         #
#     str: lambda x: f"رشته '{x}' با طول {len(x)} کاراکتر",
#     list: lambda x: f"لیست با {len(x)} عضو",
#     float: lambda x: f"عدد اعشاری {x} گرد شده: {round(x)}",
#     dict: lambda x: f"دیکشنری با کلیدهای: {list(x.keys())}"
# }
# def multi_dispatch(methods_dict):
#     def dispatcher(arg):
#         typ = type(arg)
#         if typ in arg : 
#             method = methods_dict[typ]
#             return method(arg)
#         else :
#             return "unknown type"
#     return dispatcher

# def error_handler(func, handlers_dict)          #89  shakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk  