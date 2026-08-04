import numpy as np

arr=np.array([[1,2,3],[4,5,6],
                [7,8,9],[10,11,12]])
print(arr[0])
print(arr[1])

#slicing arr[start:end:step]
print('Row selection')
print(arr[0:4])
print(arr[0:4:2])
print(arr[::2])
print(arr[::-1])

print('Column selection')
print(arr[:,1])
print(arr[0:2,0:2])
print(arr[:,::2])
print(arr[0:,1:2])