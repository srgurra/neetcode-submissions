class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map=defaultdict(list)
        for s in strs:
            s_s= "".join(sorted(s))
            strs_map[s_s].append(s)
        return [strs_map[t] for t in strs_map]
            