class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        pre = 1
        for i in range(n,1000, 1):
            for j in str(i):
                pre = pre * int(j)
            if pre % t == 0:
                return i
            pre = 1