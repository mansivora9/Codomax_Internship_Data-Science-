# importing numpy
import numpy as np

print("NumPy imported successfully!")

# creating arrays
arr1 = np.array([10,20,30,40,50])

print(arr1)

# taking array information
print("Dimensions :", arr1.ndim)
print("Shape :", arr1.shape)
print("Size :", arr1.size)
print("Data Type :", arr1.dtype)

# array indexing
print(arr1[0])
print(arr1[2])
print(arr1[-1])

# array slicing
print(arr1[1:4])
print(arr1[:3])
print(arr1[2:])

# mathematical operations
print(arr1 + 5)
print(arr1 * 2)
print(arr1 / 10)
print(arr1 - 5)

# creating 2D Array
arr2 = np.array([[1,2,3],
                 [4,5,6]])

print(arr2)

# shape of 2D Array
print(arr2.shape)
print(arr2.ndim)
print(arr2.size)

# reshaping
arr3 = np.arange(12)
print(arr3)
print(arr3.reshape(3,4))