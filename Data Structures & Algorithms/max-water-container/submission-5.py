class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rightmax = 0
        leftmax=0
        ans=0
        i=0
        j= len(heights)-1

        while i<j:
            ans= max(ans, (j-i)* (min(heights[i], heights[j])))
            if heights[i]< heights[j]:
                i+=1
            else:
                j-=1

        return ans


