class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l =0
        r = len(heights)-1
        max_water =0

        while l< r:
            h = min(heights[l],heights[r])
            w = r-l
            current_water =h*w
            max_water= max(max_water,current_water)
            if heights[l]< heights[r]:
                l+=1
            else:
                r-=1
        return max_water            

        

    
        