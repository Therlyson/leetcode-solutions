from typing import List

#problem 26 leetcode
def removeDuplicates(nums: List[int]) -> int:
    l = 0 
    r = 1
    output = 1

    while(r < len(nums)):
        if(nums[r] != nums[l]):
            nums[l+1], nums[r] = nums[r], nums[l+1]
            output += 1
            l += 1
            r += 1
        else:
            r += 1
    return output

print(removeDuplicates([1,1,2,2,3,4,4,5,5,6])) 