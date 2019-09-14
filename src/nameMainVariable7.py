from nameMainVariable6 import myPrint1

def myPrintf1():
    myPrint1()
    print("This is nameMainVariable7 and function is myPrintf1")
    
def myPrintf2():
    print("This is nameMainVariable7 and function is myPrintf2")
    
def main():
    print("This is nameMainVariable7 and main with name:"+ __name__)
    myPrintf1()
    myPrintf2()
    
main()