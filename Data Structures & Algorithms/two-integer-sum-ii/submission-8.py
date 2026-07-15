class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #input = numbers =[1,2,3,4]
        # target = 3

        n = len(numbers) #4

        for i in range(n):
            for j in range(i+1,n):
               if numbers[i]+numbers[j]==target:
                   return [i + 1, j + 1]

        return []