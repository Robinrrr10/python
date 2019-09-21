inx = 0

def search(nums, n):
    for i in range(len(nums)):
        if nums[i] == n:
            global inx
            inx = i
            return True
    return False

lst = [6, 23, 17, 8, 49, 15]
n = 23
if search(lst, n):
    print("Number found at index:", inx)
else:
    print("Number not fount")