class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1  2  3 4
        # 1  1  2 6
        # 24 12 4 1
        left = [1]
        print(left)
        right = [1]
        for num in nums:
            left.append(num*left[-1])
        print(left)
        for num in nums[::-1]:
            right.append(num*right[-1])
        right = right[::-1]
        print(right)
        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i+1])
        return ans