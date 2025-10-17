while True :
    print("choose the number: \t\n1)ramgozarie\t\n2)ramzgoshaie\t\n3)exite")
    choice = input("enter your number: ")
    if choice == "1":
        y = (input("enter your chr: "))
        list1 = ""
        for i in y:
            v = ord(i)*2-3
            list1 += chr(v)
        print(list1)
    if choice == "2":
        x = input("enter your chr: ")
        list2 = ""
        for c in x:
            v = (ord(c)+3)//2
            list2 += chr(v)
        print(list2)
    else :
        print("exite")