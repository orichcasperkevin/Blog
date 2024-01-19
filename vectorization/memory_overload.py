import numpy as np

# Create a very large array
large_array = np.ones((10**6, 10**6), dtype=np.float64)

# Perform an operation that duplicates the array in memory
result_array = large_array + large_array

# Note: The above operation is not an in-place operation; it creates a new array in memory.