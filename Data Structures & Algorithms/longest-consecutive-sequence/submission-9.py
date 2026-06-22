class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr=1
        ans= 0
        if len(nums)==0:
            return 0
        for i in range(1, len(nums)):
            if nums[i]== nums[i-1]+1:
                curr+=1
            elif nums[i]== nums[i-1]:
                continue
            else:
                ans= max(ans, curr)
                curr=1
        if curr==1 and ans==0:
            return curr
        return max(ans,curr) 
