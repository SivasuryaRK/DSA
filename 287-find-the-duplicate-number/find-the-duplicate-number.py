class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i ,j in a.items():
            if j > 1:
                return i