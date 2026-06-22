class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupStrings={}
        anagrams=[]
        for str1 in strs:
            sortedstr1= ''.join(sorted(str1))
            if len(str1) not in groupStrings:
                groupStrings[len(str1)]= {sortedstr1:[str1]}
            else:
                if sortedstr1 in groupStrings[len(str1)]:
                    groupStrings[len(str1)][sortedstr1].append(str1)
                else:
                    groupStrings[len(str1)][sortedstr1]=[str1]
        for grp in groupStrings:
            anagrams.extend(groupStrings[grp].values())
        return anagrams


        