class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        rows = len(s1)
        cols = len(s2)

        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True

        for i in range(rows + 1):
            for j in range(cols + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i - 1][j]
                        and s1[i - 1] == s3[i + j - 1]
                    )

                if j > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i][j - 1]
                        and s2[j - 1] == s3[i + j - 1]
                    )

        return dp[rows][cols]