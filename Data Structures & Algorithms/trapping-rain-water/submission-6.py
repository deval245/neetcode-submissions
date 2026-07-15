class Solution:
    def trap(self, height: List[int]) -> int:

        left,right = 0,len(height)-1
        maxL =maxR =water =0


        while left<right:
            if height[left]<= height[right]:
                maxL = max(maxL,height[left])
                water+= maxL-height[left]
                left+=1
            else:
                maxR = max(maxR,height[right])  
                water+= maxR-height[right]  
                right-=1
        return water        




        