from typing import List 

#problem 78 leetcode
def subsets(nums: List[int]) -> List[List[int]]:
    output = []

    def bt(partial, index):
        if index >= len(nums):
            output.append(partial.copy())
        else:
            partial.append(nums[index])
            bt(partial, index+1)

            partial.pop()
            bt(partial, index+1)       
    bt([], 0)
    return output

print(subsets([1,2,3])) 