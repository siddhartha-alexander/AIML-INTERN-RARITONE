#reshaping means changing shape of an array with changing it's data

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
new_arr=arr.reshape(3,3)
print(new_arr)

arr2=np.array([1,2,3,4,5,6])
new_arr2=arr2.reshape(2,3)
print(new_arr2)