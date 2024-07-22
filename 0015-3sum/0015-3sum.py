class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            j = i+1
            k = len(nums) - 1
            while j<k:
                if nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                else:
                    out.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1

        return out