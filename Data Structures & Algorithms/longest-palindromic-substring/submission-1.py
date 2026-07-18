class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_length = 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_length

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                current_length = right - left + 1

                if current_length > max_length:
                    start = left
                    max_length = current_length

                left -= 1
                right += 1

        for i in range(len(s)):

            expand(i, i)

            expand(i, i + 1)

        return s[start:start + max_length]