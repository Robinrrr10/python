
def sort(nums):
    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
          if nums[j] < nums[minpos]:
              minpos = j
        tmp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = tmp
                


nums = [8, 3, 7, 5, 10, 4, 2]
sort(nums)
print("After sorting:", nums) 