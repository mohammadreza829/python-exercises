x = int(input("Enter a number: "))                                         #myself
print(1)
for i in range(1, x):
    p = (i*2)-1  # جمله وسطه
    q = 1
    while q < p:
        print(f"{q}", end=(" "))
        q += 2
        if q==p :
            while q> 1 :
                print(f"{q}", end=(" "))
                q -= 2
            print(1)
            break
     






   




# n = 4  # تعداد ردیف‌ها                                 #chat gpt

# for i in range(1, n + 1):
#     row_numbers = []
    
#     # ۱. ساختن بخش صعودی (اعداد رو به بالا)
#     for j in range(1, 2 * i, 2):
#         row_numbers.append(str(j))
        
#     # ۲. ساختن بخش نزولی (اعداد رو به پایین)
#     for j in range((2 * i) - 3, 0, -2):
#         row_numbers.append(str(j))
        
#     # ۳. چاپ کردن کل ردیف با فاصله‌گذاری










# x = int(input("Enter a number: "))
# print(" " * (x - 1) + "1")  # اولین سطر: به اندازه x-1 فاصله و سپس عدد 1

# for i in range(1, x):
#     p = (i * 2) - 1  # جمله وسط
#     q = 1
#     # محاسبه تعداد فاصله های قبل از سطر: هرچه سطر پایین‌تر، فاصله کمتر
#     spaces = " " * (x - i - 1)
#     line = ""  # برای ذخیره اعداد این سطر به صورت رشته
    
#     while q < p:
#         line += str(q) + " "
#         q += 2
#         if q == p:
#             while q > 1:
#                 line += str(q) + " "
#                 q -= 2
#             line += "1"
#             break
    
#     # چاپ فاصله ها و سپس اعداد سطر
#     print(spaces + line)
