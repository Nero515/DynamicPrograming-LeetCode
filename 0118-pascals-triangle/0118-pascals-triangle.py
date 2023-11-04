import numpy as np
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        full_list = []
        for i in range(1, numRows+1):
            temp = np.ones(i, np.int64)
            if i > 2:
                for j in range(1, i-1):
                    temp[j] = temp_previous[j-1] + temp_previous[j]
            temp_previous = temp
            full_list.append(temp)
        return full_list