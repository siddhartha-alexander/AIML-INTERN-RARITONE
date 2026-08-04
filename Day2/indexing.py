import numpy as np
print('for 1D Array')
l1=np.array([1,2,3])
print(l1[0])
print(l1[1])
print(l1[2])

print('For 2D Array')
l2=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(l2)):
    for j in range(3):
        print(l2[i][j])

print('For 3D Array')
l3=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
             [['J','K','L'],['M','N','O'],['P','Q','R']]])
word=l3[0,0,1]+ l3[0,1,1]+l3[0,2,0]
print(word)