from typing import List 

#problem 46 leetcode
def permute(nums: List[int]) -> List[List[int]]:
    output = []

    def bt(partial):
        if len(partial) == len(nums):
            output.append(partial[::])
        else:
            for i in nums:
                if i in partial:
                    continue
                bt(partial+[i])
    bt([])
    return output

print(permute([1,2,3]))