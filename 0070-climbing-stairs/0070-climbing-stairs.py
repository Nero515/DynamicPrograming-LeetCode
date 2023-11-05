class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        n_comb = [0, 1, 2]
        for i in range(3, n + 1):
            n_comb.append(n_comb[i-1] + n_comb[i-2])
        return n_comb[-1]