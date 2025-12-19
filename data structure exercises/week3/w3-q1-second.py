input_num = list(map(float, input().replace(",", " ").split()))
n = len(input_num)
for j in range(n - 1):
    if input_num[j] > input_num[j + 1]:
        input_num[j], input_num[j + 1] = input_num[j + 1], input_num[j]
sorted_flag = True
for k in range(n - 1):
    if input_num[k] > input_num[k + 1]:
        sorted_flag = False
        break
if sorted_flag:
    print("YES")
else:
    print("NO")
