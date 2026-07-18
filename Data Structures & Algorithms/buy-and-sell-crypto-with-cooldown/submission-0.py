class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = float("-inf")
        rest = 0

        for price in prices:
            previous_hold = hold
            previous_sold = sold
            previous_rest = rest

            hold = max(
                previous_hold,
                previous_rest - price
            )

            sold = previous_hold + price

            rest = max(
                previous_rest,
                previous_sold
            )

        return max(sold, rest)