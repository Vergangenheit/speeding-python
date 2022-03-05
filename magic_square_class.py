import math
import os
import random
import re
import sys
from typing import List


class MagicSquare:
    def __init__(self, arr: List[List]):
        self.common_val = None
        self.arr = arr

    def get_rows_sum(self):
        self.row_sums = [sum(i) for i in self.arr]
        assert len(self.row_sums) == len(self.arr)

    def get_col_sums(self):
        self.col_sums = []
        for i in range(len(self.arr)):
            self.col_sums.append(self.arr[0][i] + self.arr[1][i] + self.arr[2][i])

        assert len(self.col_sums) == len(self.arr)

    def get_diags_sums(self):
        self.diag_sums = []
        self.diag_sums.append(sum([self.arr[i][i] for i in range(len(self.arr))]))
        self.diag_sums.append(sum(self.arr[i][len(self.arr) - 1 - i] for i in range(len(self.arr))))

        assert len(self.diag_sums) == 2

    @staticmethod
    def most_common(lst: List[int]) -> int:
        return max(set(lst), key=lst.count)

    def get_common_val(self):
        # parse together
        new: List[int] = self.row_sums + self.col_sums + self.diag_sums
        self.common_val = MagicSquare.most_common(new)

    @staticmethod
    def condition(x: int, common_val: int):
        return x != common_val

    @staticmethod
    def get_off_index(list_sum: List, common_val: int) -> List[int]:
        # extract index of row whose sum is != common_value
        output = [idx for idx, element in enumerate(list_sum) if MagicSquare.condition(element, common_val)]
        return output

    def main(self):
        # Write your code here
        assert len(self.arr) == len(self.arr[0])
        # analyze rows
        self.get_rows_sum()
        # analyze columns
        self.get_col_sums()
        # extract diagonal sums
        self.get_diags_sums()
        print(self.row_sums)
        print(self.col_sums)
        print(self.diag_sums)
        # extract most frequent value to aspire to
        self.get_common_val()
        print(f"Most common value is {self.common_val}")
        # extract rows who are off
        off_row = MagicSquare.get_off_index(self.row_sums, self.common_val)
        print(f"Off row indices are {off_row}")
        off_col = MagicSquare.get_off_index(self.col_sums, self.common_val)
        print(f"Off column indices are {off_col}")
        off_diag = MagicSquare.get_off_index(self.diag_sums, self.common_val)
        print(f"Off diagonals are {off_diag}")


if __name__ == '__main__':
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    magic_sq = MagicSquare(s)
    magic_sq.main()
