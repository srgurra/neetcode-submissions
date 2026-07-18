class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int, visited: set) -> None:
            visited.add((row, col))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and (next_row, next_col) not in visited
                    and heights[next_row][next_col] >= heights[row][col]
                ):
                    dfs(next_row, next_col, visited)

        for col in range(cols):
            dfs(0, col, pacific)

        for row in range(rows):
            dfs(row, 0, pacific)

        for col in range(cols):
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, cols - 1, atlantic)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result