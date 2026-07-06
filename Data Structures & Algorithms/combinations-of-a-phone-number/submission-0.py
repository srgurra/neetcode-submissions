class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ans = []
        curr = []

        def backtrack(index):
            if index == len(digits):
                ans.append("".join(curr))
                return

            digit = digits[index]

            for char in mappings[digit]:
                curr.append(char)
                backtrack(index + 1)
                curr.pop()

        backtrack(0)
        return ans