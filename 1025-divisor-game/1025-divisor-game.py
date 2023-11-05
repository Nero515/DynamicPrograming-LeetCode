class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        
        def get_x(n: int) -> int:
            for i in range(1, n):
                if n % i == 0:
                    return i
        
        x = get_x(n)
        new_n = n - x
        flag = self.divisorGame(new_n)
        if flag == False:
            return True
        else:
            return False