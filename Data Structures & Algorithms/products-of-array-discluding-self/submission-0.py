class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        result=[1]*len(nums)

        for i in range(len(nums)-1):
            j=i+1
            left[j]= left[i]*nums[i]
        

        i = len(nums)-1
        while i>0:
            j=i-1
            right[j]= right[i]*nums[i]
            i-=1

        for i in range(len(nums)):
            result[i]= left[i]*right[i]

        return result




        