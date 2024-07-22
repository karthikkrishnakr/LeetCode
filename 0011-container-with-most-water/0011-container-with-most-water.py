class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if area < height[left] * (right-left):
                    area = height[left] * (right-left)
                left+=1
            else:
                if area < height[right] * (right-left):
                    area = height[right] * (right-left)
                right-=1
        return area