def simple_calc(num_lst):
    if not num_lst:
        return "Error: Invalid Input"
    str_lst = [str(item) for item in num_lst]
    operator_index = None
    for i, item in enumerate(str_lst):
        if item == "+":
            operator_index = i
            break
    if operator_index is None:
        return "Error: Invalid Input"
    if operator_index == 0:
        return "Error: Invalid Sequence"
    if operator_index == len(str_lst) - 1:
        return "Error: Invalid Sequence"
    left_numbers = "".join(str_lst[:operator_index])
    if not left_numbers.isdigit():
        return "Error: Invalid Input"
    left_value = int(left_numbers)
    right_numbers = "".join(str_lst[operator_index + 1 :])
    if not right_numbers.isdigit():
        return "Error: Invalid Input"
    right_value = int(right_numbers)
    result = left_value + right_value
    return [int(x) for x in str(result)]


user_input = input()
tokens = []
curr = ""
in_number = False
for c in user_input:
    if c.isdigit():
        curr += c
        in_number = True
    else:
        if in_number:
            tokens.append(int(curr))
            curr = ""
            in_number = False
        if c == "+":
            tokens.append("+")
if curr:
    tokens.append(int(curr))
result = simple_calc(tokens)
print(result)
