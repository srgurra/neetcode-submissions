class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]

            longest = 1

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[new_row][new_col] > matrix[row][col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(new_row, new_col)
                    )

            memo[(row, col)] = longest
            return longest

        answer = 0

        for row in range(rows):
            for col in range(cols):
                answer = max(answer, dfs(row, col))

        return answer