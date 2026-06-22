class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j= len(heights)-1
        ans=left= right= 0

        while i<j:
            left= max(left, heights[i])
            right= max(right, heights[j])
            min1= min(left, right)
            
            ans= max(ans, min1*(j-i))
            print(min1, j, i)
            if heights[i]< heights[j]:
                i+=1
            else:
                j-=1

        return ans

