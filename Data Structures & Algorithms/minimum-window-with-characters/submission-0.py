class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map= Counter(t)
        left=0
        ans=0
        have= 0
        required= len(t_map)
        temp = defaultdict(int)
        minlen= math.inf
        ans=[-1,-1]
        for right in range(len(s)):
            ch= s[right]
            temp[ch]+=1

            if ch in t_map and temp[ch]== t_map[ch]:
                have+=1
            while have== required:
                if right-left+1< minlen:
                    minlen= right-left+1
                    ans= [left, right]
                leftchar= s[left]
                temp[leftchar]-=1
                if leftchar in t_map and temp[leftchar] < t_map[leftchar]:
                    have -= 1
                left+=1
        l, r= ans
        return "" if minlen == float("inf") else s[l:r+1]

            