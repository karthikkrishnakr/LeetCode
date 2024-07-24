class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        out.append(1)
        for i in range(1,len(nums)):
            out.append(out[i-1]*nums[i-1])
        out2 = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            out2[i]=out2[i+1]*nums[i+1]
            out[i]*=out2[i]
        return out