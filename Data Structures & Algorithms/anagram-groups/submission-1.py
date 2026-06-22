class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams= {}
        for st in strs:
            if ''.join(sorted(st)) in anagrams:
                anagrams[''.join(sorted(st))].append(st)
            else:
                anagrams[''.join(sorted(st))] = [st]
        return [anagrams[i] for i in anagrams]