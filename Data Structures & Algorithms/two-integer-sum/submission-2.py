class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        l= list()
        for i in range(len(nums)):
            if target -nums[i] in numsMap:
                l= [numsMap[target -nums[i]], i]
                break
            numsMap[nums[i]]= i
        return l
        