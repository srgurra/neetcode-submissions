class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr= nums[0]
        maxSum= nums[0]

        for num in nums[1:]:
            curr= max(curr+num, num)
            maxSum = max(maxSum, curr)
        return maxSum

