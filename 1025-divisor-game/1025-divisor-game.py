class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        x = 1
        new_n = n - x
        flag = self.divisorGame(new_n)
        if flag == False:
            return True
        else:
            return False