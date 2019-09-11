
print("pattern 1")
for n in range(4): 
    for i in range(4):
        print("#", end = "")
    print()

print("pattern 2")
for n in range(4):
    for i in range(n + 1):
        print("#", end = "")
    print()
    
print("pattern 3")
for n in range(4):
    for i in range(4 - n):
        print("#", end = "")
    print()