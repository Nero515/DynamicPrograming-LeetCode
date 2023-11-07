class Solution:
    def countVowelStrings(self, n: int) -> int:
        init_sol = [1] * 5
        for i in range(n-1):
            for j in range(1, 5):
                init_sol[j] = init_sol[j] + init_sol[j-1]
            
        return sum(init_sol)
            