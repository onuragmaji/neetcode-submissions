from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        q1 = deque()
        num_rotten = 0
        num_fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                   q1.append((r,c))
                   num_rotten+=1
                if grid[r][c]==1:
                    num_fresh+=1

        mins=-1
        dir_list = [(0,-1),(0,1),(-1,0),(1,0)]
        while q1:
              size = len(q1)
              mins+=1
              for i in range(size):
                  r,c = q1.popleft()
                  for dr,dc in dir_list:
                      if dr+r>=0 and dr+r<rows and dc+c>=0 and dc+c<cols:
                         if grid[r+dr][c+dc]==1:
                            grid[r+dr][c+dc]=2
                            num_fresh-=1
                            q1.append((dr+r,dc+c))
        if num_fresh!=0:
           return -1
        if num_fresh==0 and num_rotten==0:
           return 0    
        return mins                     








        