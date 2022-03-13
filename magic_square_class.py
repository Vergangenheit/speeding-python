import math
import os
import random
import re
import sys
from typing import List
from collections import OrderedDict

"""
1- get sums (rows, columns , diagonals).
put row sums, column sums and diagonal sums into a single iterable data structure linking sums to their elements;
2- from sums get the most common value(the target):
3- get indices of rows, columns , diagonals who are off the target and by how much;
4- find a way to iterate over iterable datastructure;
"""


class MagicSquare:
    def __init__(self, arr: List[List]):
        self.common_val = None
        self.arr = arr
        self.ds_row = []
        self.ds_col = []
        self.ds_diag = []
        self.u_ds = []

    def get_rows_sum(self):
        self.row_sums = [sum(i) for i in self.arr]
        for row in self.arr:
            t = (sum(row), row)
            self.ds_row.append(t)

        assert len(self.row_sums) == len(self.arr)

    def get_col_sums(self):
        self.col_sums = []
        for i in range(len(self.arr)):
            s: int = self.arr[0][i] + self.arr[1][i] + self.arr[2][i]
            t = (s, [self.arr[0][i], self.arr[1][i], self.arr[2][i]])
            self.ds_col.append(t)
            self.col_sums.append(s)

        assert len(self.col_sums) == len(self.arr)

    def get_diags_sums(self):
        self.diag_sums = []
        lr_diag = [self.arr[i][i] for i in range(len(self.arr))]
        rl_diag = [self.arr[i][len(self.arr) - 1 - i] for i in range(len(self.arr))]
        self.diag_sums.append(sum(lr_diag))
        self.diag_sums.append(sum(rl_diag))
        self.ds_diag.append((sum(lr_diag), lr_diag))
        self.ds_diag.append((sum(rl_diag), rl_diag))

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
    def gap(x: int, common_val: int) -> int:
        return abs(x - common_val)

    @staticmethod
    def get_off_index(list_sum: List, common_val: int) -> (List[int], List[int]):
        # extract index of row whose sum is != common_value
        output = [idx for idx, element in enumerate(list_sum) if MagicSquare.condition(element, common_val)]
        gaps = []
        for out in output:
            gaps.append(abs(list_sum[out] - common_val))
        return output, gaps

    def mesh_ds(self):
        # put the three comprehensive datastructures together
        self.u_ds = self.ds_row + self.ds_col + self.ds_diag

    def change_axes(self, index_row: int, index_col: int, target: int):
        # change one of the values to achieve target
        # ex: row
        val: int = self.arr[index_row][index_col]

    def main(self):
        # Write your code here
        assert len(self.arr) == len(self.arr[0])
        # analyze rows
        self.get_rows_sum()
        # analyze columns
        self.get_col_sums()
        # extract diagonal sums
        self.get_diags_sums()
        print(self.ds_row)
        print(self.ds_col)
        print(self.ds_diag)
        # extract most frequent value to aspire to
        self.get_common_val()
        print(f"Most common value is {self.common_val}")
        # extract rows who are off
        off_row, row_gaps = MagicSquare.get_off_index(self.row_sums, self.common_val)
        print(f"Off row indices are {off_row} by {row_gaps}")
        off_col, col_gaps = MagicSquare.get_off_index(self.col_sums, self.common_val)
        print(f"Off column indices are {off_col} by {col_gaps}")
        off_diag, diag_gaps = MagicSquare.get_off_index(self.diag_sums, self.common_val)
        print(f"Off diagonals are {off_diag} by {diag_gaps}")
        # self.change_axes(off_row[0], off_col[0], self.common_val)
        self.mesh_ds()
        print(self.u_ds)


if __name__ == '__main__':
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    magic_sq = MagicSquare(s)
    magic_sq.main()
