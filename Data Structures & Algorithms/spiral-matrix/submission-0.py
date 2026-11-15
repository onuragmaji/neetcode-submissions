class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        UP,DOWN,LEFT,RIGHT = 0,1,2,3
        lt_wall = -1
        rt_wall = cols
        bt_wall = rows
        up_wall = 0

        DIRECTION  =  RIGHT
        result = []
        i,j=0,0 
        while len(result)!=rows*cols:
            if DIRECTION == RIGHT and len(result)!=rows*cols:
                while j<rt_wall:
                    result.append(matrix[i][j])
                    j+=1
                rt_wall-=1
                j=rt_wall
                i+=1
                DIRECTION = DOWN
                print(result,i,j)

            if DIRECTION == DOWN and len(result)!=rows*cols:
                while i < bt_wall:
                    result.append(matrix[i][j])
                    i+=1  
                bt_wall-=1
                i=bt_wall
                j-=1
                DIRECTION = LEFT
                print(result,i,j)

            if DIRECTION == LEFT and len(result)!=rows*cols:
                while j>lt_wall:
                    result.append(matrix[i][j])
                    j-=1
                lt_wall+=1
                j=lt_wall
                i-=1
                DIRECTION = UP
                print(result,i,j)

            if DIRECTION == UP and len(result)!=rows*cols:
                while i>up_wall:
                    result.append(matrix[i][j])
                    i-=1
                up_wall+=1
                i=up_wall
                j+=1
                DIRECTION = RIGHT
                print(result,i,j)  

        return result      









                     
                      
                 



            


                 
                 



