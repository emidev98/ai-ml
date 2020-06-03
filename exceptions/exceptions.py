def divide_list_elements(list,dividend):
    try:
        return [i/dividend for i in list]
    except ZeroDivisionError as e:
        return list


data_list = list(range(5))
zero = 0
two = 2

print(divide_list_elements(data_list,two))
print(divide_list_elements(data_list,zero))