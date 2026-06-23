class TimeMap:

    def __init__(self):
        self.nums=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.nums[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        nums_list= self.nums[key]

        i=0
        j= len(nums_list)-1
        ans= ""
        while (i<=j):
            mid = (i+j)//2
            print(mid, i, j)
            if nums_list[mid][1]<= timestamp:
                ans= nums_list[mid][0]
                i= mid+1
            else:
                j= mid-1
        return ans
        
