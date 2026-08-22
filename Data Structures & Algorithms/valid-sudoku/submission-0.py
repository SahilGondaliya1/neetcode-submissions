class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [["1","2","3","4","5","6","7","8","9"] for _ in range(9)]
        column = [["1","2","3","4","5","6","7","8","9"] for _ in range(9)]
        grid = [["1","2","3","4","5","6","7","8","9"] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                print(i , j)
                if board[i][j] == ".":
                    continue

                sub_box = 0
            
                if i < 3 and j < 3:
                    sub_box = 0
                    
                elif i < 3 and j < 6:
                    sub_box = 1
                    
                elif i < 3 and j < 9:                    
                    sub_box = 2
                    
                elif i < 6 and j < 3:
                    sub_box = 3
                    
                elif i < 6 and j < 6:
                    sub_box = 4
                    
                elif i < 6 and j < 9:                    
                    sub_box = 5
                    
                elif i < 9 and j < 3:
                    sub_box = 6
                    
                elif i < 9 and j < 6:
                    sub_box = 7
                    
                elif i < 9 and j < 9:                    
                    sub_box = 8
                        
                    
                if (board[i][j] not in row[i]) or (board[i][j] not in column[j]) or (board[i][j] not in grid[sub_box]) :
                    return False
                
                row[i].remove(board[i][j])
                
                column[j].remove(board[i][j])
                
                
                grid[sub_box].remove(board[i][j])

        return True
