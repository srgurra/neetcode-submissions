class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]* len(temperatures)
        stack=[]
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0]< temp:
                _, ind1= stack.pop()
                res[ind1]= ind- ind1
            stack.append((temp, ind))
        return res


            