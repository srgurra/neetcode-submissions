class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m= defaultdict(int)
        res=[]
        reverse = defaultdict(list)
        for num in nums:
            m[num]+=1
        for n in m.keys():
            reverse[m[n]].append(n)
        maxfreq = max(reverse.keys())
        i=0
        while i< k:
            if maxfreq in reverse:
                res.extend(reverse[maxfreq])
                i+=len(reverse[maxfreq])
            maxfreq-=1
            
        return res
            
