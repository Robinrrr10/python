from numpy import *
arr1 = array([12, 43, 66, 17, 4, 92, 24])
for i in arr1:
    print("Value is:", i)

arr2 = array([23, 67, 12])
arr2 = arr2 + 5
print("value of arr2 after adding 5 is:", arr2)

arr3 = array([2, 12, 20, 11])
arr4 = array([21, 1, 5, 9])
arr5 = arr3 + arr4
print("After adding two array value of arr5 is:", arr5)

arr6 = array([2, 4, 36 ,12, 15])
print("sin of each values in arr6:", sin(arr6))
print("cos of each values in arr6:", cos(arr6))
print("log of each values in arr6:", log(arr6))
print("square root of each values in arr6:", sqrt(arr6))
print("mininum value in arr6:", min(arr6))
print("maximum value in arr6:", max(arr6))
print("sum of all values in arr6:", sum(arr6))

arr7 = array([23, 81, 22, 11])
arr8 = array([7, 61, 37, 90, 12])
arr9 = concatenate([arr7, arr8])
print("combined array is:", arr9)

arr10 = array([5, 11, 3, 23, 7])
arr11 = arr10
print("array arr10 is:", arr10)
print("Copied arr11 is:", arr11)
print("memory address of arr10 is:", id(arr10))
print("memory address of copied arr11 is:", id(arr11))

arr12 = array([4, 15, 12, 81, 34])
arr13 = arr12.view()
print("array arr12 is:", arr12)
print("Copied arr13 is:", arr13)
print("memory address of arr12 is:", id(arr12))
print("memory address of copied arr13 is:", id(arr13))

arr12[2] = 66
print("now(after changing value of arr12[2]) array arr12 is:", arr12)
print("now(after changing value of arr12[2]) Copied arr13 is:", arr13)
print("now(after changing value of arr12[2]) memory address of arr12 is:", id(arr12))
print("now(after changing value of arr12[2]) memory address of copied arr13 is:", id(arr13))



arr14 = array([13, 4, 12, 8, 20])
arr15 = arr14.copy()
print("array arr14 is:", arr14)
print("Copied arr15 is:", arr15)
print("memory address of arr14 is:", id(arr14))
print("memory address of copied arr15 is:", id(arr15))

arr14[2] = 55
print("now(after changing value of arr14[2]) array arr14 is:", arr14)
print("now(after changing value of arr14[2]) Copied arr15 is:", arr15)
print("now(after changing value of arr14[2]) memory address of arr14 is:", id(arr14))
print("now(after changing value of arr14[2]) memory address of copied arr15 is:", id(arr15))






