from anonymousOrLambdaFuction import square
def myvalue():
    return 4

v1 = myvalue()
print("V1 is:", v1)

def myvalue2():
    yield 6

v2 = myvalue2()
print("V2 is:", v2)
print("value in V2 is:", v2.__next__())

def myValues3():
    yield 34
    yield 12
    yield 54
    yield 29

v3 = myValues3()
print("value in V3 is:", v3.__next__())
print("value in V3 is:", v3.__next__())
print("value in V3 is:", v3.__next__())

def myVal4():
    num = 4
    while num <= 10:
        sq = num * num
        yield sq
        num += 1
        
v4 = myVal4()
for k in v4:
    print("value in V4 is:", k)


