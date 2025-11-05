def stack_based_addition(input_list):
    if not input_list:
        return "Error: Invalid Input"

    plus_index = -1
    for idx, item in enumerate(input_list):
        if item == "+":
            plus_index = idx
            break

    if plus_index == -1:
        return "Error: Invalid Input"
    if plus_index == 0 or plus_index == len(input_list) - 1:
        return "Error: Invalid Sequence"

    left_digits = "".join(str(x) for x in input_list[:plus_index])
    right_digits = "".join(str(x) for x in input_list[plus_index + 1 :])

    if not left_digits.isdigit() or not right_digits.isdigit():
        return "Error: Invalid Input"

    sum_result = int(left_digits) + int(right_digits)

    return [int(d) for d in str(sum_result)]


user_input = input()
tokens = []
str_n = ""
numm = False
for c in user_input:
    if c.isdigit():
        str_n += c
        numm = True
    else:
        if numm:
            tokens.append(int(str_n))
            str_n = ""
            numm = False
        if c == "+":
            tokens.append("+")
if str_n:
    tokens.append(int(str_n))
result = stack_based_addition(tokens)
print(result)
