x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
for i in range(1,x+1):
    if x % i == 0 and y % i == 0:
        print(i)
#______________________بزرگترین مقسوم الیه__________________
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
        print(i)
        break










