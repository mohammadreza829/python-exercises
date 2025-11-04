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
        return "Error: No + operator found"
    if operator_index == 0:
        return "Error: Operator at start"
    if operator_index == len(str_lst) - 1:
        return "Error: Operator at end"

    left_numbers = "".join(str_lst[:operator_index])
    if not left_numbers.isdigit():
        return "Error: Invalid left numbers"
    left_value = int(left_numbers)

    right_numbers = "".join(str_lst[operator_index + 1 :])
    if not right_numbers.isdigit():
        return "Error: Invalid right numbers"
    right_value = int(right_numbers)

    return left_value + right_value


# استفاده مستقیم از لیست پایتون (بدون input)
test_list = [9, 9, 9, "+", 5]
print(f"Test list: {test_list}")

result = simple_calc(test_list)
print("Result:", result)
if isinstance(result, int):
    res = [int(x) for x in str(result)]
    print("Result as list:", res)
