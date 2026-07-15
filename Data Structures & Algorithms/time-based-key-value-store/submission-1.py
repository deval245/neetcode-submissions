from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        entries = self.store[key]
        res = ""

        l,r = 0,len(entries)-1
        while l<= r:
            mid = (l+r)//2

            if entries[mid][0]<= timestamp:
                res = entries[mid][1]
                l+=1
            else:
                r-=1
        return res            


        
