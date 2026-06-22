class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        m= {
            '}':'{',
            ']':'[',
            ')': '('
        }
        for ch in s:
            if ch in m and stack and stack[-1]== m[ch]:
                stack.pop()
            else:
                stack.append(ch)
        return not stack
        