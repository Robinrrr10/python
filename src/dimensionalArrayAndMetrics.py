from numpy import *
arr1 = array([
    [2, 1, 4],
    [3, 8, 5]
    ])
print("2 dimensional array arr1 is:\n", arr1)
print("dimension of array arr1 is:", arr1.ndim)
print("shape of array arr1 is:", arr1.shape)
print("size(number of element) of array arr1 is:", arr1.size)
arr2 = arr1.flatten()
print("2 dimension converted to 1 dimension array arr2 is:\n", arr2)

arr3 = array([2, 4, 7, 1, 3, 2, 7, 4])
arr4 = arr3.reshape(2, 4)  # 2 row with 4 column
print("created one dimension array to 2 dimension with 2 row and 4 column:\n", arr4)

arr5 = array([6, 14, 7, 1, 31, 2, 6, 4, 12, 3, 15, 3])
arr6 = arr5.reshape(2, 2, 3)
print("from 1 dimensional array, two 2 dimensional (3D array) array is created:\n", arr6)


arr7 = array([
    [8, 4, 5, 6],
    [5, 1, 9, 4]
    ])
mtx1 = matrix(arr7) # here array arr7 is converted to matrix
print("matrix mtx1 is:\n", mtx1)

mtx2 = matrix('5 2 12 9 ; 1 3 8 2')
print("matrix mtx2 is:\n", mtx2)

mtx3 = matrix('3 1 ; 11 8 ; 2 9 ; 1 7')
print("matrix mtx3 is:\n", mtx3)

mtx4 = matrix('3 1 8; 2 8 5; 4 1 7')
print("matrix mtx4 is:\n", mtx4)
print("matrix mtx4 diagonal value is:", diagonal(mtx4))
print("matrix mtx4 min value is:", mtx4.min())
print("matrix mtx4 max value is:", mtx4.max())

mtx5 = matrix('4 9 8; 4 4 1; 5 2 6')
mtx6 = matrix('2 1 9; 2 5 9; 8 5 7')
print("matrix mtx5 is:\n", mtx5)
print("matrix mtx6 is:\n", mtx6)
mtx7 = mtx5 + mtx6
print("Addition of two matrix is:\n", mtx7)
mtx8 = mtx5 - mtx6
print("substraction of two matrix is:\n", mtx8)
mtx9 = mtx5 * mtx6
print("multiplication of two matrix is:\n", mtx9)









