class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = []
        first = min(nums)
        for i in range(first, max(nums)+1):
            if i not in nums:
                a.append(i)
        return a