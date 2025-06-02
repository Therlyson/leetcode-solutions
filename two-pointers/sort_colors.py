from typing import List

#problem 75 leetcode
def sortColors(nums: List[int]) -> None:
    l = 0
    r = len(nums) - 1
    minimo = min(nums)

    while l <= r:
        if(nums[l] > minimo and nums[r] == minimo):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        else:
            if(nums[l] == minimo):
                l += 1
            if(nums[r] != minimo):
                r -= 1
                
    r = len(nums) - 1
    if 2 in nums[l:r+1]:
        while l <= r:
            if(nums[l] == 2 and nums[r] == 1):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if(nums[l] == 1):
                l += 1
            if(nums[r] != 1):
                r -= 1
    return nums

print(sortColors([2,0,2,1,1,0]))