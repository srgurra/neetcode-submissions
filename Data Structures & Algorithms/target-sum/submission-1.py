from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, curr):
            if i<0:
                return target== curr
            ways=0
            for j in (-1, 1):
                ways+= dp(i-1, curr+nums[i]*j)
                    
            return ways
        return dp(len(nums)-1, 0)