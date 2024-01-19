import numpy as np



#1 Element-wise operations.Addition, subtraction, multiplication, division, exponentiation, etc.

harry = np.array([89, 70, 66, 40])
mary = np.array([50, 67, 78, 81])
dan = np.array([56, 45, 90, 92])
tracey = np.array([56, 24, 9, 23])

result = harry+mary+dan+tracey
print(result)
# #addition 
# result = a + b
# #print(result)


# #universal functions eg sin,cos,exp.
# angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
# sine_values = np.sin(angles)
# print(sine_values)


# #aggreagation functions.
# #Functions like np.sum(), np.mean(), np.max(), np.min(), etc., can operate on entire arrays or along specific axes.
# total = np.sum(a)
# print(total)


# #logical operations.
# mask = (a == b)
# mask2 = (a > b)
# print(mask,mask2)