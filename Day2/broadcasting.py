import numpy as np

#Broadcasting allows numpy to perform operations on array
#with different shapes by virtually expanding dimensions
#so they match the larger arrays shape

# the dimensions have the same size
#OR
#one of the dimensions has a size of 1

arr1=np.array([[1,2,3,4]])
arr2=np.array([[1],[2],[3],[4]])
print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)

#it will throws an error because the rows and columns are not compatible or neither one
arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=np.array([[1],[2],[3],[4]])
print(arr1*arr2)