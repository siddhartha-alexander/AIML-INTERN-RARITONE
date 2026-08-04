import numpy as np

n1=np.array('A')
print(n1.ndim)

n2=np.array(['A','B','C'])
print(n2.ndim)

n3=np.array([[1,2,3],[4,5,6]])
print(n3.ndim)

n4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(n4.ndim)