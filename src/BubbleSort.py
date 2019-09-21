
def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                


nums = [8, 3, 7, 5, 10, 4, 2]
sort(nums)
print("After sorting:", nums) 