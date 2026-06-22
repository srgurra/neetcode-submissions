class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            set1= set()
            for j in range(0,9):
                if board[i][j]!='.' and board[i][j] in set1:
                    return False
                set1.add(board[i][j])
        for i in range(0,9):
            set1= set()
            for j in range(0,9):
                if board[j][i]!='.' and board[j][i] in set1:
                    return False
                set1.add(board[j][i])
        i=0
        j=0
        for k in range(0,9,3):
            for l in range(0,9,3):
                set1= set()
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if board[i][j]!='.' and board[i][j] in set1:
                            return False
                        set1.add(board[i][j])
            
        return True
            
            


                
        