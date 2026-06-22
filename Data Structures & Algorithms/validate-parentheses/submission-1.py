class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets_map= {')':'(', '}':'{', ']': '['}
        for ch in s:
            if stack and ch in brackets_map:
                if stack.pop()!= brackets_map[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0