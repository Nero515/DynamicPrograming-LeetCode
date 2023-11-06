class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        j = 0
        i = 0
        letter = s[0]
        while j < len(t):
            if letter == t[j]:
                i += 1
                if i < len(s):
                    letter = s[i]
                else:
                    return True
            j += 1
        return False