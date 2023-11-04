from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = {}
        n_rows = len(triangle)
        if n_rows == 1:
            return triangle[0][0]
        element_num = 0
        previous_el_num = 0
        for i in range(n_rows-2, -1, -1):
            current_row = triangle[i]
            next_row = triangle[i+1]
            for j in range(len(current_row)):
                if element_num - previous_el_num in mem.keys():
                    left_sum = current_row[j] + min(mem[element_num-previous_el_num])
                    right_sum = current_row[j] + min(mem[element_num-previous_el_num+1])
                else:
                    left_sum = current_row[j] + next_row[j]
                    right_sum = current_row[j] + next_row[j+1]
                mem[element_num] = [left_sum, right_sum]
                element_num += 1
            previous_el_num = len(current_row)
        return min(mem[element_num-1])
            
            