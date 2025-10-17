# --------------------------------------list--------------------------------------------
# x = [1,2,3]       #1
# print(x)

# x2 = ["bob", "alice" , "charlie"]     #2
# print(x2[0])

# x3 = ["blue" , "green" , "red"]   #3
# print(x3[2])
#
# x4 = [10,20,30]       #4
# print(len(x4))

# x5 = ["cherry" , "banana", "apple"]     #9
# print(len(x5))

# x6 = [5,15,10]    #10
# print(max(x6))

# x7 = [100,200,300]    #11
# print(min(x7))

# x8 = [2,3 , "python", "js"]     #12
# print(x8)

# x9 = "python"         #13
# print(list(x9))

# x10 = [1,2,3]     #15
# print(list(x10))

# x11=[ "red", "green", "blue" , "yellow" ]     #17
# print(x11[2:4])

# x12 = ["aylin", "mohammad","reza", "ali", "hossein"]      #18
# print(x12[0:3])

# x13 = [1,2,3,4,5,6,7,8,9]     #19
# print(x13[-1])

# x14 = [1,2,3,4,5]     #20
# print(x14[0: :2])

# x15 = [1,2,3,4,5]     #21
# x15[1]=90
# print(x15)

# x16 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]       #23
# x16[13:15]=[20,30]
# print(x16)

# x17= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]        #24
# print(x17[::-1])

# x18 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]        #27
# x18.append(16)
# print(x18)

# x19 = ["apple", "banana", "cherry"]        #28
# y = ["orange", "kiwi", "pineapple"]
# print(x19.extend(y))

# x20 = [1,2,3]         #29
# x20.insert(1,4)
# print(x20)

# x21 = [1,2,3]         #30
# x21.remove(2)
# print(x21)

# x22= [1,2,3]         #31
# y= x22.pop(0)
# print(x22)
# print(y)

# x23=[1,2,3]         #32
# x23.clear()
# print(x23)

# x24 = [1,2,3,4,5,6,7,8,9,10,11]       #54
# x24[2:6]=[11,12,13,14,15,16]
# print(x24)

# x25 = [1,2,3,4,5,6,7,8]     #55
# del(x25[1:5])
# print(x25)

# x26 = [1,2,3,4,5,6,7,8,9,10]        #24
# print(x26[::-1])

# x27 = [10,9,8,7,6,5,4,3,2,1]      #33
# x27.sort()
# print(x27)

# x28 = [1 , 2 ,3,4,5,6,7,8,9,10]      #34
# x28.sort(reverse=True)
# print(x28)

# x29 = [1,2,3,4,5,6,7,8,9,10]      #56
# x29.reverse()
# print(x29)

# x30 = [10,9,8,7,6,5,4,3,2,1]  #57
# x30.sorted()
# print(x30)

# x31 = [10,9,8,8,8,7,7,6,7,6,5,4,3,2,1]  #37
# y= x31.count(8)
# print(y)

# x32 = [10,9,8,7,6,5,4,3,2,1]  #38
# y = x32.index(1)
# print(y)

# x33 = [10,9,8,7,6,5,4,3,2,1]    #53
# print(8 in x33)

x34 = [10,9,8,7,6,5,4,3,2,1]  #40 shakkkkk
y = " ".join(map(str, x34))
print(y)

# x35 = (10,9,8,7,6,5,4,3,2,1)  #42 shakkkkk , 43 , 52
# y = " ".split(x35)
# print(y)

# x36 = [1,2,[3,4,5]]   #50
# print(x36[2][1])

# x37 = [1,2,[3,4,5]]     #39
# y = x37.copy()
# print(y)

# x38 = [1,2,[3,4,5]]       #47
# y = [6,7,8]
# y1 = y+x38
# print(y1)

# x39 = ["salam" , "ahmad" , "reza" , "ali"]      #59
# item1 , item2 , *item3 = x39
# print(item1)

# --------------------------------------------------------------------tuples-----------------------------------------------------------------

# x40 = (1,2,3)   #1
# print(x40)

# x41 = ("bob", "alice", "charlie" )   #2
# print(x41[0])

# x42 = ("blue", "green", "red")   #3
# print(x42[-1])

# x43 = (10,20,30)        #4
# print(len(x43))

# x44= ("apple", "banana", "cherry")   #9
# print(type(x44))

# x45=(5,15,10)       #10
# print(max(x45))

# x46 = (10,20,(30,50,40),(40,20))   #12
# print(x46)

# x47 = "python"      #13
# print(tuple(x47))

# x48 = ("python", "banana")  #15
# print(tuple(x48))

# x49 = ("red" , "green" , "blue")   #17
# print(x49[1:3])

# x50 = (1,2,3,4,5,6,7,8,9,10)   #18
# print(x50[0:3])

# x51 = (1,2,3,4,5,6,7,8,9,10)    #19
# print(x51[-1])

# x52 = (1,2,11,4,5,6,7,8,9,10)    #20
# print(x52[0::2])

# x53 = (1,2,3,4,5)             #21 important
# y = list(x53)
# y[1]=99
# x53 = tuple(y)
# print(x53)

# x54 = (1,2,3,4,5,6,7,8,9,10)    #22 important
# y = list(x54)
# y.reverse()
# y.append(0)
# y.reverse()
# x54 = tuple(y)
# print(x54)

# x55 = (1,2,3,4,5,6,7,8,9,10)    #23 important
# y = list(x55)
# y[8:10]=[20,30]
# x55 = tuple(y)
# print(x55)

# original_tuple = (1, 2, 3, 4, 5)          #23   raveshe 2
# print(f"تاپل اولیه: {original_tuple}")
# # یک تاپل جدید می‌سازیم که شامل تمام عناصر به جز دو عنصر آخر است،
# # و سپس تاپل جدید (10, 20) را به انتهای آن اضافه می‌کنیم.
# new_tuple = original_tuple[:-2] + (10, 20)
# print(f"تاپل جدید: {new_tuple}")

# x56 = (1,2,3)     #29
# y = list(x56)
# y.insert(1,22)
# x56 = tuple(y)
# print(x56)

# x57 = (1,2,3)     #30
# y = list(x57)
# y.remove(2)
# x57 = tuple(y)
# print(x57)

# x58 = "python"      #37
# print(tuple(x58))

# x59 = tuple(range(5))     #38
# print(x59)

# x60 = (1,2,3,4,5,6,7)     #41
# y = list(x60)
# print(y)

# x61={1,2,3,4,5,6,7}     #51
# y = tuple(x61)
# print(y)

# x62= [10,9,8,7,6,5,4,]        #56 shakkk
# y = x62.sorted()
# print(y)

# x63 = {'name': 'Alice', 'age': 25, 'city': 'New York'}      #57
# print(tuple(x63.keys()))

# x64=(1,2,3,4,5,60)        #25
# p1 , p2 , p3 , *p4 = x64
# print(p4)

# x65 = (1,2,3,4,5,(6,7),8)     #46
# print(x65[5])

# x66 = (1,2,3,4,5,6,7)         #52
# print(x66[1:])

# x67 = (1,2,3,4)       #28
# y=(5,6,7,8)
# print(x67+y)

# x68 = (1,2,3,40)      #34
# print(max(x68))

# x69 = ("salam", "mmd", "khoobi") #39 important
# print(" ".join(x69))

# x70 = (1,2,3,4,5)     #43
# print(sum(x70))

# x71 = (1,2,3,4)       #46
# y = x71 * 7
# print(y)

# ----------------------------------------------------------------------sets-----------------------------------------------

# x72 = {1,2,3,4,5}     #1
# print(x72)

# x73 = {"bob", "alice", "charles"}     #2
# print(x73)

# x74="python"          #13
# print(set(x74))

# x75 = [1,2,2,3,3]       #30
# print(set(x75))

# print(set(range(5)))    #34

# x76 = {"apple", "banana", "cherry"}       #19
# x76.add("mango")
# print(x76)

# x77 = {"red", "green", "blue", "yellow"}      #17
# x77.remove("red")
# print(x77)

# x78 ={"red", "green", "blue", "yellow"}       #18
# x78.discard("yellow")
# print(x78)

# x79 = {1, 2, 3}                # 20
# x79.update([4, 5, 6])  
# print(x79)

# x80 = {1, 2, 3}           # 22
# x80.clear()  
# print(x80)

# x81 = {1,2,3,4,5,6,7,8,9,10}            #23 imp
# y= {12,13,14,15,16,17,18,19,20}
# print(x81.union(y))

# x82 = {1,2,3,4,5,6,7,8,9,10}            #24 imp
# y = {1,2,3,4,51}
# print(x82.intersection(y))

# x83 = {1,2,3,4,5,6,7,8,9,10}            #25 imp
# y = {1,2,3,4,51}
# print(x83.difference(y))

# x84 = {1,2,3,4,5,6,7,8,9,10}            #26 imp
# y = {1,2,3,4,51}
# print(x84.symmetric_difference(y))

# x85 = {1,2,3,4,5,6,7,8,9,10}            
# print(x85.pop())

# x86= {1,2,3,4,5,6,7,8,9,10}         #27   
# y = {1,2,3,4,5}
# print(y.issubset(x86))

# x87 = {1,2,3,4,5,6,7,8,9,10}         #28
# y = {1,2,3,4,5}
# print(x87.issuperset(y))

# x88 = {1,2,3,4,5,6,7,8,9,10}         #29
# y = {1,2,3,4,5}
# print(y.isdisjoint(x88))

# x89 = {1,1,1,1,2,2,2,3,3,3,3}       #41
# print(x89)

# x90 = (1,2,3,4,5)       #42
# print(set(x90))

# x92 = {1:"mmd", 2:"khoobi", 3:"salam"}    #43
# print(set(x92)) 


# x93 = {1:"mmd", 2:"khoobi", 3:"salam"}    #44
# print(set(x93.values()))

# x94 = {"mmd", "khoobi", "salam"}    #35
# y = " ".join(x94)   
# print(y)

# x95 = {"mmd", "khoobi", "salam"}    #36
# x95.copy()
# print(x95)

# x96 = {"mmd", "khoobi", "salam"}    #37
# frozenset(x96)
# print(x96)

# x97 = {1,2,3,4,5,6}       #48
# y = {4,5,6,7,8,9}
# print(x97.difference(y))

# x98 = {1,2,3,4,5,6}       #49
# y = {4,5,6,7,8,9}
# print(x98.symmetric_difference(y))

# x99 = {1,2,3,4,5,6}       #50
# y = {4,5,6,7,8,9}
# y2 = {4,5,6,7,8,9,10}
# print(x99.intersection(y , y2))

# x100 = [1,2,3,4,5]        #56
# y = [4,5,6,7,8]
# y2 = set(x100) |set(y)
# print((y2))

# x101 = {1,2,3,4,5}       #59
# y = {4,5,6,7,8}
# y2 = x101 - y
# print(y2)

# x102 = {1,2,3,4,5}       #53
# y = {4,5,6,7,8}
# x102.difference_update(y)
# print(x102)

# x103 = {1,2,3,4,5}       #54
# y = {4,5,6,7,8}
# x103.intersection_update(y)
# print(x103)   

#-----------------------------------------------------------------------------dictitionary-----------------------------------------------

# x104 = {"first_name":"mmd", "last_name":"khoobi"}    #1
# print(x104)

# x105 = {"first_name":"mmd", "last_name":"khoobi"}    #3
# print(x105["first_name"])

# x106 = {"first_name":"mmd", "last_name":"khoobi"}    #9
# print(type(x106))

# x107 = {"first_name":"mmd", "last_name":"khoobi"}    #14
# print(x107.get("first_name"))

# x108 = {"first_name":"mmd", "last_name":"khoobi"}    #15
# print("first_name" in x108)

# x109 = {"first_name":"mmd", "last_name":"khoobi"}    #11
# print(x109.keys())

# x110 = {"first_name":"mmd", "last_name":"khoobi"}    #12
# print(x110.values())

# x111 = {"first_name":"mmd", "last_name":"khoobi"}    #13 imp imp
# print(x111.items())

# x112 = {"first_name":"mmd", "last_name":"khoobi"}    #16
# x112["last_name"] = "fasli"
# print(x112)

# x113 = {"first_name":"mmd", "last_name":"khoobi"}    #17
# x113["city"] = "shiraz"
# print(x113)

# x114 = {"first_name":"mmd", "last_name":"khoobi"}    #18
# x114.pop("first_name")
# print(x114)

# x115 = {"first_name":"mmd", "last_name":"khoobi"}    #19
# x115.popitem()  
# print(x115)

# x116 = {"first_name":"mmd", "last_name":"khoobi"}    #21
# x116.copy()
# print(x116)

# x117 = {"first_name":"mmd", "last_name":"khoobi"}    #22
# y= {"city":"shiraz"}
# x117.update(y)
# print(x117)

# x118 = ["a","b","c"]        #25
# y = [1,2,3]
# print(dict(zip(x118,y)))

# x119=[("a",1),("b",2),("c",3)]        #26
# print(dict(x119))

# print(dict(a=1,b=2,c=3))

# x120 = ["first_name", "last_name" ] #27 ////////////////////
# values = 0
# dict.fromkeys(x120,values)
# print(x120)

# x121 = ["first_name", "last_name" ] #28
# values = "mmd"
# dict.fromkeys(x121,values)
# print(x121)