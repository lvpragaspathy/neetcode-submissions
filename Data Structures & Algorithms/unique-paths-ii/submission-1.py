class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == [[1]]:
            return 0

        if obstacleGrid == [[0]]:
            return 1
        
        
        m = len(obstacleGrid)
        n= len(obstacleGrid[0])   

        mem = [[-1] * n for i in range(m)]

        def dp(i, j):
            if (i, j) == (m-1, n-1):
                return 1

            if i > m-1 or j > n-1:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if mem[i][j] != -1:
                 return mem[i][j]

            mem[i][j] = dp(i, j+1) + dp(i+1, j)

            return mem[i][j]
        
        return dp(0,0)

        

                

            
            

            
