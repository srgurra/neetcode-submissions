class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(curr, opencount, closecount):
            if opencount==n and closecount==n:
                ans.append(curr[:])
                return

            if opencount<n:
                curr.append('(')
                backtrack(curr, opencount+1, closecount)
                curr.pop()

            if closecount<opencount:
                curr.append(')')
                backtrack(curr, opencount, closecount+1)
                curr.pop()
        ans=[]
        backtrack([], 0, 0)
        ans= ["".join(a) for a in ans]
        return ans
        