# IMPORTANT. run this command prompt as like below
#python getInputWhileRunningPythonFile.py 10 20
print("IMPORTANT: run this in command prompt or terminal as like below")
print("python getInputWhileRunningPythonFile.py 10 20")
import sys
size = len(sys.argv)
print("length of command is:", size)

if size == 3:    
    a = sys.argv[1]   # argv[0] is the filename
    b = sys.argv[2]
    x = int(a)
    y = int(b)
    print("Addition of two values is:", x + y)
else:
    print("run this program only in command prompt or terminal as like below")
    print("python getInputWhileRunningPythonFile.py 10 20")
    
    
