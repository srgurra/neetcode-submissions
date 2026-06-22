class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def duplicates_in_list(list2):
            nums = [x for x in list2 if x != "."]
            return len(nums) != len(set(nums))
        for i in range(len(board)):
            if duplicates_in_list(board[i]):
                print("yes duplicates", board[i])
                return False
        print("rows clean")
        for i in range(9):
            list1=[]
            for j in range(9):
                list1.append(board[j][i])

            if duplicates_in_list(list1):
                return False
        print("columns clean")
        for r in range(0,9,3):
            for c in range(0,9,3):
                list1=[]
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        list1.append(board[i][j])
                if duplicates_in_list(list1):
                    return False
        print("boxes clean")
        return True