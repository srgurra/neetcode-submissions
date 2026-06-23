class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            ch=0
            for p in piles:
                ch+= math.ceil(p/k)
            return ch<=h

        low=1
        high= max(piles)

        while low<=high:
            mid= (high+low)//2
            if check(mid):
                high= mid-1
            else:
                low= mid+1
        return low
            