import numpy as np
import time

# Generate a large array of random strings
large_array_strings = np.array(['abc', 'def', 'ghi'] * (10**5))

# Slow Python loop to perform character-wise manipulation
def slow_string_manipulation_loop(array):
    result = np.empty_like(array, dtype=object)
    for i in range(len(array)):
        result[i] = array[i].upper()
    return result

# Vectorized operation using NumPy's vectorize function
vectorized_string_manipulation = np.vectorize(lambda x: x.upper())

# Measure time for the slow loop
start_time = time.time()
result_slow_loop = slow_string_manipulation_loop(large_array_strings)
slow_loop_time = time.time() - start_time

# Measure time for the vectorized operation
start_time = time.time()
result_vectorized = vectorized_string_manipulation(large_array_strings)
vectorized_time = time.time() - start_time

# Compare times
print(f"Time taken by slow loop: {slow_loop_time} seconds")
print(f"Time taken by vectorized operation: {vectorized_time} seconds")
