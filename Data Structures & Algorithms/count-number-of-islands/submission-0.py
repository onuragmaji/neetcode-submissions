class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        iland_count=0
        dir_list = [(0,-1),(0,1),(-1,0),(1,0)]
        def dfs(r,c):
            for dr,dc in dir_list:
                if dr+r>=0 and dr+r<rows and dc+c>=0 and dc+c<cols and grid[dr+r][dc+c]=='1': 
                   grid[dr+r][dc+c]='0'
                   dfs(dr+r,dc+c)
            return 0             
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                   print(grid[r][c]) 
                   iland_count+=1
                   dfs(r,c) 
        return iland_count