class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if not heights: return 0

        l,r =0 ,len(heights)-1
        water =0

        while l< r:
            h = min(heights[l], heights[r])
            w =r-l
            water = max(water,h*w)
            if heights[l]< heights[r]:
                l+=1
            else:
                r-=1
        return water            