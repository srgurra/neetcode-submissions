class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(path,curr, i):
            if curr== target:
                ans.append(path[:])
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if curr+candidates[j]<=target:
                    curr+= candidates[j]
                    path.append(candidates[j])
                    backtrack(path, curr, j+1)
                    curr-=candidates[j]
                    path.pop()
        ans=[]
        backtrack([], 0, 0)
        return ans