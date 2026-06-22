class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        m= len(grid)
        n= len(grid[0])
        directions= [[0,1], [0,-1], [1,0], [-1,0]]

        graph = deque([0,0])
        seen= set()
        def valid(row, col):
            return 0<= row< m and 0<= col< n and grid[row][col]== '1'
        def dfs(row, col):
            for dx, dy in directions:
                currrow, currcol= row+ dx, col+ dy
                if valid(currrow, currcol) and (currrow, currcol) not in seen:
                    seen.add((currrow, currcol))
                    dfs(currrow, currcol)
                    

        ans=0
        for i in range(m):
            for j in range(n):
                if valid(i,j) and (i,j) not in seen:
                    seen.add((i, j))
                    dfs(i,j)
                    ans+=1
                    
        return ans

