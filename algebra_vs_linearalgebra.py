import numpy as np

# Multiply two arrays 
x = [1,2,3]
y = [2,3,4]
product = []
for i in range(len(x)):
    product.append(x[i]*y[i])
    
# Linear algebra version (3x faster)
x = np.array([1,2,3])
y = np.array([2,3,4])
x * y
