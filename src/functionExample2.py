def change(val):
    print("memory address of val before change:", id(val))
    val = 10
    print("memory address of val after change:", id(val))
    print("val is:", val)

n = 45
print("memory address of n before calling:", id(n))
print("value of n before calling:", n)
change(n)
print("memory address of n after calling:", id(n))
print("value of n after calling:", n)


def changeList(listVal):
    print("memory address of listVal before change:", id(listVal))
    listVal[1] = 22
    print("memory address of listVal after change:", id(listVal))
    print("listVal is:", listVal)
    
mlist = [10, 20, 30, 40]
print("memory address of mlist before calling:", id(mlist))
print("value of mlist before calling:", mlist)
changeList(mlist) # Below also list will change even update in function
print("memory address of v after calling:", id(mlist))
print("value of n after calling:", mlist)