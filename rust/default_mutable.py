# def append_to_list(value, my_list=[]):
#     my_list.append(value)
#     return my_list

# list1 = []
# result1 = append_to_list(1,list1)
# print(result1)  # Output: [1]

# result2 = append_to_list(2)
# print(result2)  # Output: [1, 2]

# result3 = append_to_list(3)
# print(result3)  # Output: [1, 2, 3]


def modify_list(lst):       
    lst.append(4)    
    lst.clear()
    lst += [1, 2, 3]    


my_list = [1, 2, 1]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3]
