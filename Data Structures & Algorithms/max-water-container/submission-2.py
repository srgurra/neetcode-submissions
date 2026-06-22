class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j= len(heights)-1
        ans=0

        while i<j:

            min1= min(heights[i], heights[j])
            
            ans= max(ans, min1*(j-i))
            if heights[i]< heights[j]:
                i+=1
            else:
                j-=1

        return ans

