def my_gen():
    num=0
    num2=1
    x= input("choose p/n :")
    if x=="p":
        while True:
            yield num
            num += 2
    elif x=="n":
        while True:
            yield num2
            num2+=2


for q in my_gen() :
    print(q)
