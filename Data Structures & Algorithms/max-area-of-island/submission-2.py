class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        dir_lookup = [(0,-1),(0,1),(-1,0),(1,0)]
        ctr = 0
        def dfs(r,c):
            area=1
            for dr,dc in dir_lookup:
                if dr+r>=0 and dr+r<rows and dc+c>=0 and dc+c<cols and grid[dr+r][c+dc]==1:
                   grid[dr+r][c+dc]=0
                   area+=dfs(dr+r,dc+c)
            return area  
        max_len = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                   grid[r][c]=0 
                   max_len = max(max_len,dfs(r,c)) 
                   
        # print(grid)           
        return max_len