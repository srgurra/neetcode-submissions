class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap={}
        returnList=[]
        for i in range(len(nums)):
            if (target-nums[i]) not in diffmap:
                diffmap[nums[i]]=i
            else:
                returnList= [diffmap[target-nums[i]],i]
                break                
        
        return returnList
                  


        