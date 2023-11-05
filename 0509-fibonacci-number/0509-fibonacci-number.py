class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        if n == 1:
            return 1
        elif n == 0:
            return 0
        arr = [0,1]
        for i in range(2, n+1):
            x = arr[-1] + arr[-2]
            arr.append(x)
        return arr[-1]