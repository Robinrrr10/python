
nums = [3, 23, 67, 12, 48, 8, 27]
for i in nums:
    print("number is:", i)
    
myit = iter(nums)
print("my iterator each num:",myit.__next__())
print("my iterator each num:",myit.__next__())
print("my iterator each num:",myit.__next__())
print("my iterator each num:",myit.__next__())
print("directly calling next num:",next(myit))
print("directly calling next num:",next(myit))


class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
    
tp1 = TopTen()

print(tp1.__next__())
print(tp1.__next__())
print(tp1.__next__())

for j in tp1:
    print("j is:", j)

