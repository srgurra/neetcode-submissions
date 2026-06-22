class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set= set(nums)
        maxlength=0
        for n in nums:
            length=0
            if n-1 not in nums_set:
                while n+length in nums_set:
                    length+=1
            maxlength= max(length, maxlength)
        return maxlength
            
                


        