def simple_calc(num_lst):
    if not num_lst:
        return "Error: Invalid Sequence"

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
        return "Error: Calculation Error"
    left_value = int(left_numbers)

    right_numbers = "".join(str_lst[operator_index + 1 :])
    if not right_numbers.isdigit():
        return "Error: Calculation Error"
    right_value = int(right_numbers)

    result = left_value + right_value
    return [int(x) for x in str(result)]


user_input = input("enter your list :")

test_list = eval(user_input)
result = simple_calc(test_list)
print(result)
