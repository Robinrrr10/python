from array import *
count = int(input("How many number need to inserted:"))
myarray = array('i', [])
for i in range(count):
    x = int(input("Enter input number:"))
    myarray.append(x)

print("You array is:", myarray)
choise = int(input("Please enter 1 or 2 \n1.Search number using index\n2.Find index of number\nAnswer:"))
if choise==1:
    inx = int(input("Enter index:"))
    if inx < len(myarray) and inx >= 0 :
        print("Index ", inx, " has number:", myarray[inx])
    else:
        print("Invalid index")
elif choise==2:
    num = int(input("Enter number:"))
    arrInx = 0
    for e in myarray:
        if e == num:
            print("Index of number ", num, " is:", arrInx)
            break
        arrInx += 1
    else:
        print("Number not found")
else:
    print("Invalid input")
    