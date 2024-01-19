import numpy as np



#1 Element-wise operations.Addition, subtraction, multiplication, division, exponentiation, etc.
# employee = [S,M,L,XL]

harry = [89, 70, 66, 40]
mary = [50, 67, 78, 81]
danny = [56, 45, 90, 92]
tracey = [56, 24, 9, 23]

#pay per box size
 

harry = np.array(harry)
mary = np.array(mary)
danny = np.array(danny)
tracey = np.array(tracey)
pay = {"S": 20, "M": 40, "L": 80, "XL": 160}

def calculate_total(item,pay):
    return item * pay

custom_ufunc = np.frompyfunc(calculate_total, 2, 1)

pay_per_size = custom_ufunc(
        tracey,
        np.array( list(pay.values())) 
    )
print(pay_per_size)

total = np.sum(pay_per_size)
print(total)

# total_boxes = harry + mary + danny + tracey
# print(total_boxes)
# #addition 
# result = a + b
# #print(result)

# arrays = np.array([harry,mary,danny,tracey])
# # Extract elements at index 3 (the XL boxes) from each row
# xl_boxes = arrays[:, 3]
# index_of_highest_value = np.argmax(xl_boxes)
# print(index_of_highest_value)



# #universal functions eg sin,cos,exp.
# angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
# sine_values = np.sin(angles)
# print(sine_values)


# #aggreagation functions.
# #Functions like np.sum(), np.mean(), np.max(), np.min(), etc., can operate on entire arrays or along specific axes.
# total = np.sum(tracey)
# print(total)
