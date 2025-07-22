def longestSubarray(nums: list[int]) -> int:
        l = 0
        zero_count = 0
        max_len = 0
        
        for r, val in enumerate(nums):
            if val == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            max_len = max(max_len, r - l)
        
        return max_len


#Outra solução
# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         l = 0
#         r = 0
#         partial = nums[l:r+1]
#         maxVet = 0
#         qtdZero = partial.count(0)

#         if 0 not in nums:
#             return len(nums) - 1
            
#         while(r < len(nums)):
#             if(qtdZero < 2):
#                 if len(partial) > maxVet:
#                     maxVet = len(partial)
#                 r += 1
#             else:
#                 l += 1
#             partial = nums[l:r+1]
#             qtdZero = partial.count(0)
            
#         return maxVet-1 