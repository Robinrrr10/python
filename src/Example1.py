def getNumCount(nums):
    oddCount = 0
    evenCount = 0
    for j in nums:
        if j % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return oddCount,evenCount
n = [23, 1, 67, 82, 2, 55, 20, 56, 2]
oCount, eCount = getNumCount(n)
print("Number of even:{} and number of odd:{}".format(eCount,oCount))

def getAllNum(nums):
    odd = []
    even = []
    for j in nums:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    return odd, even
allOdd, allEven = getAllNum(n)
print("Even number are:", allEven)
print("Odd number are:", allOdd)