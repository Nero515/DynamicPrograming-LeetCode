class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        arr = [1] * n
        for i in range(1, n):
            val = arr[i]
            for j in range(i - 1, -1, -1):
                temp = arr[j]
                if s[i] == s[j]:
                    arr[j] = 2 + val if j+1 <= i-1 else 2
                else:
                    arr[j] = max(arr[j+1], arr[j])
                val = temp
        return arr[0]