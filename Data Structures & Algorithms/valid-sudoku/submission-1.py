class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] # rows[r] keeps digits seen at row r
        columns = [set() for _ in range(9)] * 9 # columns[c] keeps digits seen at col c
        squares = [set() for _ in range(9)] * 9 # squares[(r // 3) * 3 + (c // 3)] keeps digits in the 3x3 box
        
        def getIndex(row: int, column: int) -> int:
            return (row // 3) * 3 + (column // 3)

        for r in range(9):        
            for c in range(9):
                if board[r][c] == '.':
                    continue

                digit = board[r][c]

                if digit in rows[r]:
                    return False
                elif digit in columns[c]:
                    return False
                elif digit in squares[getIndex(r, c)]:
                    return False
                else:
                    rows[r].add(digit)
                    columns[c].add(digit)
                    squares[getIndex(r, c)].add(digit) 
                
        return True
            



            

                






        
        
        
        
        return True       