class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set= set(nums)
        max1=0
        for i in nums_set:
            j=1
            local_max=1
            while(i+j in nums_set):
                j+=1
            max1= max(max1, j)
        return max1
        