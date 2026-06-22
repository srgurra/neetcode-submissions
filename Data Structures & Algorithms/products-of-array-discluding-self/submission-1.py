class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix1= [1]* (len(nums)+1)
        prefix2= [1]* (len(nums)+1)
        for i in range(len(nums)):
            prefix1[i+1]= prefix1[i]* nums[i]
        print(prefix1)
        for i in range(len(nums)-1, -1, -1):
            prefix2[i]= prefix2[i+1]* nums[i]
        print(prefix2)
        res= [1]* len(nums)
        for i in range(len(nums)):
            res[i]= prefix1[i]*prefix2[i+1]
        return res