# binary search works only when collection is in order
inx = 0

def search(nums, n):
    l = 0
    u = len(nums) - 1
    while l <= u:
        mid = (l + u) // 2
        if nums[mid] == n:
            globals()['inx'] = mid
            return True
        else:
            if nums[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False
        
    
    
lst = [5, 17, 23, 28, 34, 41, 54, 59, 68, 72, 90]
n = 54
if search(lst, n):
    print("Number found at index:", inx)
else:
    print("Number not fount")