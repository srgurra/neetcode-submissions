class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set= set()
        left= right=ans=0

        while right< len(s):
            while s[right] in s_set:
                s_set.remove(s[left])
                left+=1
            s_set.add(s[right])
            ans= max(ans, right-left+1)
            right+=1
        return ans