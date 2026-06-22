class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list=[]
        already_parsed=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] ==0:
                        triplet = [nums[i],nums[j],nums[k]]
                        triplet.sort()
                        if (triplet not in already_parsed):
                            
                            ans_list.append([nums[i],nums[j],nums[k]])
                            already_parsed.append(triplet)
        return ans_list