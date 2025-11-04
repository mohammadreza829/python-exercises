def simple_calc(num_lst):
   
    operator_index = None
    for i, item in enumerate(num_lst):
        if not isinstance(item, int):
            operator_index = i
            # if operator_index == 0:
            #     return "Error: Invalid Sequence"
            # elif operator_index != "+" :
            #     return "Error: Calculation Error"
            break
    
    if operator_index is None:
        return None
    
    
    left_numbers = ''.join(str(x) for x in num_lst[:operator_index])
    left_value = int(left_numbers)
    
   
    right_numbers = ''.join(str(x) for x in num_lst[operator_index+1:])
    right_value = int(right_numbers)
    
    
    operator = num_lst[operator_index]
    if operator == '+':
        return left_value + right_value



num = [9, 9, 9, '+', 5]
result = simple_calc(num)
print("نتیجه:", result)  # خروجی: 1004