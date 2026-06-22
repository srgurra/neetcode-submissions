class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for st in strs:
            res+= str(len(st))+'#'+st
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        res=[]
        i=0
        while i< len(s):
            j=i
            while s[j]!= '#':
                j+=1
            l= int(s[i:j])
            res.append(s[j+1: j+l+1])
            i= j+l+1
        return res           
            
            


