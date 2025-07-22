#problem 53
def maxSubArray(nums: list[int]) -> int:
    memo = [0] * len(nums)
    memo[0] = nums[0]
    max_output = nums[0]

    for i in range(1, len(nums)):
        memo[i] = max(nums[i], nums[i] + memo[i-1])
        max_output = max(memo[i], max_output)
    return max_output

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# [-2, 1,-3, 4,-1, 2, 1, -5, 4]
# [-2, 1, -2, 4, 3, 5, 6, 1, 5] memo