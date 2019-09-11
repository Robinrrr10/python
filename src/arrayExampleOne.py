from array import *
values = array('i', [ 67, 12, -45, 4, 19 ]) # i is for integer
print("values are:", values)
print("address and size type is:", values.buffer_info())
print("datatype(typecode) is:", values.typecode)
print("first value is", values[0], " second value is", values[1])
print("Total lenght(size) of arrays is: ", len(values))
i = 0
while i < len(values):
    print("index ", i, "value is:", values[i])
    i += 1
    
for n in range(len(values)):
    print(n, "index and value:", values[n])

for k in values:
    print("Each value is:", k)

#nwa = array('I', [2, 4, 12, -9, 45]) # I is only support possitive integer
#print("values are", nwa)

vn = array('i', [ 9, 16, 50, 33, 12, 78])
vn.reverse()
print("reverse values:", vn)

mych = array('u', ['j', 'c', 'x', 'd'])
print("characters array:", mych)

bn = array('i', [89, 23, 2, 78, 17, 44])
newarr = array(bn.typecode, (a for a in bn))
print("copied array is:", newarr)
anotherArr = array(bn.typecode, ( n * n for n in bn))
print("square in copied array", anotherArr)



