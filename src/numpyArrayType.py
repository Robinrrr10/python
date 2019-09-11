from numpy import *
ar = array([1, 3, 5, 6])
print("array ar is:", ar)
print("datatype of array ar is:", ar.dtype)

ar2 = array([3, 5.3, 6, 12, 56,11, 4])# as one float value is there it will convert to float
print("array ar2 is:", ar2)
print("datatype of ar2 is:", ar2.dtype)

ar3 = array([2, 1, 34, 11, 6], float)
print("array ar3 is:", ar3)
print("datatype of ar3 is:", ar3.dtype)

ar3 = linspace(0, 16)
print("array ar3 is:", ar3)

ar4 = linspace(0, 16, 17)
print("array of ar4 is:", ar4)

ar5 = linspace(2, 10, 4)
print("array ar5 is:", ar5)

ar6 = linspace(21, 30, 10)
print("array ar6 is:", ar6)

ar7 = linspace(21, 30, 5)
print("array ar7 is:", ar7)

ar8 = arange(10)
print("array ar8 is:", ar8)

ar9 = arange(11, 20)
print("array ar9 is:", ar9)

ar10 = arange(1, 15, 2)
print("array ar10 is:", ar10)

ar11 = arange(40, 53, 3)
print("array ar11 is:", ar11)

ar12 = logspace(1, 40, 5)
print("array ar12 is:", ar12)
print("array ar12 first value is:", ar12[0])
print("array ar12 first value is: %.2f" %ar12[0])
print("array ar12 fourth value is:", ar12[3])
print("array ar12 fourth value is: %.3f" %ar12[3])

ar13 = zeros(6)
print("array ar13 is: ", ar13)

ar14 = ones(5)
print("array ar14 is:", ar14)

ar15 = ones(7, int)
print("array ar15 is:", ar15)










