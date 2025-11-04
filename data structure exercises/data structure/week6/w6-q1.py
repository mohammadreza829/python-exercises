def parse_input_list(s):

    s = s.strip()
    if s[0] == "[" and s[-1] == "]":
        s = s[1:-1]

    tokens = s.split(",")

    out = []
    for tok in tokens:
        tok = tok.strip()

        if (tok.startswith("'") and tok.endswith("'")) or (
            tok.startswith('"') and tok.endswith('"')
        ):
            tok = tok[1:-1]
        if tok == "+":
            out.append("+")
        elif tok.isdigit():
            out.append(int(tok))
        else:
            print("Error: Invalid Input in list!")
            exit()
    return out


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
    if operator_index == 0 or operator_index == len(str_lst) - 1:
        return "Error: Invalid Sequence"
    left_numbers = "".join(str_lst[:operator_index])
    right_numbers = "".join(str_lst[operator_index + 1 :])
    if not left_numbers.isdigit() or not right_numbers.isdigit():
        return "Error: Calculation Error"
    left_value = int(left_numbers)
    right_value = int(right_numbers)
    result = left_value + right_value
    return [int(x) for x in str(result)]


inp = input()
user_list = parse_input_list(inp)
result = simple_calc(user_list)
print(result)
