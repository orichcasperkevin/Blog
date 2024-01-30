import timeit
from functools import partial

def unique_list_using_lists(list1,list2):
    result = []
    for item in list1 + list2:
        if item not in result:
            result.append(item)
    return result

def unique_list_using_sets(list1,list2):
    result = set()
    for item in list1 + list2:
        if item not in result:
            result.add(item)
    return list(result)

list1 = list(range(0,1_000))
list2 = list(range(500,1_000))

# Create partially-applied functions
partial_function_lists = partial(unique_list_using_lists, list1, list2)
partial_function_sets = partial(unique_list_using_sets, list1,list2)

# Measure the execution time of partially-applied function_lists
time_one = timeit.timeit(partial_function_lists, number=1000)

# Measure the execution time of partially-applied function_sets
time_two = timeit.timeit(partial_function_sets, number=1000)

print("Time for function_lists:", time_one)
print("Time for function_sets:", time_two)

#Time for function_lists: 6.59087880800007

#Time for function_sets: 0.11217345100021703