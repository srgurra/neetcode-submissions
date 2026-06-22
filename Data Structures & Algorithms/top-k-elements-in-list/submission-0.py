class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqnums={}
        for i in nums:
            if i in freqnums:
                freqnums[i]+=1
            else:
                freqnums[i]=1
        freqnumssorted= dict(sorted(freqnums.items(), key=lambda x:x[1], reverse=True))

        return list(freqnumssorted.keys())[0:k]
        