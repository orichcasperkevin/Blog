import numpy as np

# Define a custom function that operates on scalars
def my_function(x):
    return x + 1

# Create a add_one from the custom function
add_one = np.frompyfunc(my_function, 1, 1)
#numpy.frompyfunc is used to create a add_one from my_function. 
#The second argument (1) is the number of input arguments, and the third argument (1) is the number of outputs.

# Create a NumPy array
arr = np.array([1, 2, 3, 4])

# Use the custom add_one on the array
result = add_one(arr)

print(result)