class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        water=0

        while left<right:
            if height[left]<=height[right]:
                leftmax=max(height[left],leftmax)
                water+=leftmax-height[left]
                left+=1
            else:
                rightmax=max(height[right],rightmax)
                water+=rightmax-height[right]
                right-=1

        return water

        
        