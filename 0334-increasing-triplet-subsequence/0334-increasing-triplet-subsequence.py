class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[j] < nums[k]:
                            return True
        return False