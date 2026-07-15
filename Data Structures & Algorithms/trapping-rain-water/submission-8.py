class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:

            return 0

        l,r =0, len(height) -1

        left_mx = height[l]
        right_mx = height[r]
        res =0

        while l<r:
            if left_mx < right_mx:
                l+=1
                left_mx = max(left_mx,height[l])
                res+=left_mx -height[l]
            else:
                r-=1
                right_mx = max(right_mx,height[r])  
                res+= right_mx -height[r]  
        return res        



           
         