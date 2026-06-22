class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for s in strs:
            strs_map["".join(sorted(list(s)))].append(s)
        return list(strs_map.values())