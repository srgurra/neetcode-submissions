class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater =0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                if maxwater < (min(heights[i], heights[j])*(j-i)):
                    maxwater = min(heights[i], heights[j])*(j-i)

        return maxwater
        