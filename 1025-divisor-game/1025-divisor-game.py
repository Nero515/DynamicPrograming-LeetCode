class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        flag = self.divisorGame(n - 1)
        if flag == False:
            return True
        else:
            return False