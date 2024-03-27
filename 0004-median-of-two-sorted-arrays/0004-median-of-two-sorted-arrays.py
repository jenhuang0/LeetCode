class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = 0
        r = len(nums1)-1

        if len(nums1)%2 ==1:
            return float(nums1[len(nums1)//2])
        else:
            ml = nums1[len(nums1)//2 -1]
            mr = nums1[len(nums1)//2 ]
            print(nums1)
            print(ml)
            print(mr)
            return (float(ml)+float(mr))/2.0
        
