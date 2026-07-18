class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for last in range(left + 1, right):
                    coins = (
                        balloons[left]
                        * balloons[last]
                        * balloons[right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][last]
                        + coins
                        + dp[last][right]
                    )

        return dp[0][n - 1]