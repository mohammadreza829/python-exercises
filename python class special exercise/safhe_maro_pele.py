count = 100
c = 1
while count > 0:
    if c% 2 == 1 :
        j = 0
        while j < 10:
            print(f"{count:3}", end=" ")
            count -= 1
            j += 1 
        print()
    else :
        j = 0
        temp = count-9
        while j < 10:
            print(f"{temp:3}", end=" ")
            temp +=1
            j += 1 
            count -=1
        print()
    c +=1
    

    