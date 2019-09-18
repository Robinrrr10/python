
f1 = open('file1.txt', 'r') # r means read
print(f1.readline()) # first line
print(f1.readline()) # second line
print(f1.read()) # give al line which is not read

f2 = open('file2.txt', 'w') # w is for writing the file. if file is not there it will create it
f2.write("Hi how are you")

f3 = open('file2.txt', 'a') # a means append
f3.write("Fine da")

# below is for copying two text file
f4 = open('file1.txt', 'r')
f5 = open('file3.txt', 'w')
for i in f4:                  # this two line is for copying two file. 
    f5.write(i)
    
#below is for copying binary files Eg: image, video etc
f6 = open('nature.jpeg', 'rb') # r means read and b means binary
f7 = open('newcopiedpic.jpeg', 'wb') # w means write and b means binary
for i in f6:
    f7.write(i)

    

    
