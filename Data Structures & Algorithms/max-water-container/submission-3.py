class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rightmax = 0
        leftmax=0
        ans=0
        i=0
        j= len(heights)-1

        while i<j:
            leftmax= max(leftmax, heights[i])
            rightmax= max(rightmax, heights[j])
            ans= max(ans, (j-i)* (min(leftmax, rightmax)))
            if heights[i]< heights[j]:
                i+=1
            elif heights[i]> heights[j]:
                j-=1
            else:
                i+=1
                j-=1

        return ans


