class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map={}
        for row in board:
            for cell in row:
                if cell!='.' and cell in row_map:
                    return False
                row_map[cell]=1
            row_map= {}

        col_map={}
        for i in range(0,9):
            for row in board:
                if row[i]!='.' and row[i] in col_map:
                    return False
                col_map[row[i]]=1
            col_map= {}

        box_map={}
        for i in range(0, 9, 3):
            for k in range(0, 9, 3):
                for j in range(i, i+3):
                    for l in range(k,k+3):
                        print(board[j][l])
                        if board[j][l]!='.' and board[j][l] in box_map:
                            return False
                        box_map[board[j][l]]=1
                box_map={} 
        
        return True


        