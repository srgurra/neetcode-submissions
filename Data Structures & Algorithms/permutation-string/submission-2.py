class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size= len(s1)
        s1_set= Counter(s1)
        if len(s1)> len(s2):
            return False
        for i in range(0, len(s2)-window_size+1):
            string1= s2[i:i+window_size]
            print(string1)
            if Counter(string1)== s1_set:
                return True
        return False
                