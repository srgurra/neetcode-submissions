class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphas={}
        for i in s:
            if i in alphas:
                alphas[i]+=1
            else:
                alphas[i]=1
        print(alphas)
        for j in t:
            if j in alphas:
                alphas[j]-=1
            else:
                alphas[j]=-1
        print(alphas)
        for k in alphas:
            if alphas[k]!=0:
                return False
        return True
        
        