class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]

                if stack:
                    w=i-stack[-1]-1
                else:
                    w=i
                maxarea=max(maxarea,h*w)

            stack.append(i)

        heights.pop()
        return maxarea

        