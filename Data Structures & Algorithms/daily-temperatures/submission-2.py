class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        n = len(T)

        res = [0]*n
        stack =[]
        for i ,num in enumerate(T):
            while stack and num> T[stack[-1]]:
                j = stack.pop()
                res[j]= i-j
            stack.append(i) 
        return res    