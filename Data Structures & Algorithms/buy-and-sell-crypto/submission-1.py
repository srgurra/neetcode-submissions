class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice= prices[0]
        ans=0

        for price in prices[1:]:
            ans= max(ans, price- minprice)
            minprice= min(minprice, price)
        return ans
