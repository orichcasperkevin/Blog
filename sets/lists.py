#creation
my_list = [1, 2, 3, 'apple', 'banana', True]

#indexing
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'apple'

#slicing
print(my_list[1:4])  # Output: [2, 3, 'apple']

#adding items and conncatenating 
my_list.append(4)
new_list = my_list + ['orange', 'grape']
print(f" list after additions : {new_list}")

#removing items
my_list.remove('banana')
my_list.pop(2)
del my_list[0]
print(f" list after deletions : {my_list}")

#length
length = len(my_list)
print(f"length is {length}")

# mutability 
my_list[0] = 99
print(f"modified list : {my_list}")