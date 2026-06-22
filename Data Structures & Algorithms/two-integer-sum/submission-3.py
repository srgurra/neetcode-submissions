class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for ind, num in enumerate(nums):
            if (target-num) in nums_map:
                return [nums_map[target-num],ind]
            nums_map[num]= ind
        return [-1,-1]
