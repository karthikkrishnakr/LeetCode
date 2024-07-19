class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = (n1+n2)//2
        i = 0
        j = 0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        if i<n1:
            while i<n1:
                nums3.append(nums1[i])
                i+=1
        else:
            while j<n2:
                nums3.append(nums2[j])
                j+=1
        if (n1+n2)%2==0:
            return (nums3[n3]+nums3[n3-1])/2
        else:
            return nums3[n3]