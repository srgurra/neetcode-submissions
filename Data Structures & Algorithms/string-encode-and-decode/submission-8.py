class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result+=str(len(st))+'#'+st

        return result

    def decode(self, s: str) -> List[str]:
        declist=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            print(s[i:j])
            length= int(s[i:j])
            declist.append(s[j+1: j+length+1])
            i= j+length+1
        return declist

