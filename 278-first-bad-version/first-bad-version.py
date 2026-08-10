# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        f,l = 1, n
        while f < l:
            m = f + (l-f) // 2
            if isBadVersion(m):
                l = m
            else:
                f = m + 1
        return f