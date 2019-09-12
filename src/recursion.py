import sys

print("Default recusionlimit is:", sys.getrecursionlimit())

#sys.setrecursionlimit(2000)  #set upto how many time can a function call itself

i = 1
def welcome():
    print("Welcome all")
    global i
    i += 1
    while(i <= 10):
        welcome()
welcome()