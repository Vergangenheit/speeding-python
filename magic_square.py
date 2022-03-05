import math
import os
import random
import re
import sys
from typing import List


def get_rows_sum(s: List[List]) -> List[int]:
    row_sums = [sum(i) for i in s]
    assert len(row_sums) == len(s)
    return row_sums


def get_col_sums(s: List[List]) -> List[int]:
    col_sums = []
    for i in range(len(s)):
        col_sums.append(s[0][i] + s[1][i] + s[2][i])

    assert len(col_sums) == len(s)
    return col_sums


def get_diags_sums(s: List[List]) -> List[int]:
    diag_sums = []
    diag_sums.append(sum([s[i][i] for i in range(len(s))]))
    diag_sums.append(sum(s[i][len(s) - 1 - i] for i in range(len(s))))

    assert len(diag_sums) == 2

    return diag_sums


def most_common(lst: List[int]) -> int:
    return max(set(lst), key=lst.count)


def get_common_val(a: List, b: List, c: List) -> int:
    # parse together

    new = a + b + c
    return most_common(new)


def formingMagicSquare(s: List[List]):
    # Write your code here
    assert len(s) == len(s[0])
    # analyze rows
    row_sums = get_rows_sum(s)
    # analyze columns
    col_sums = get_col_sums(s)
    # extract diagonal sums
    diag_sums = get_diags_sums(s)
    print(row_sums)
    print(col_sums)
    print(diag_sums)
    # extract most frequent value to aspire to
    goal: int = get_common_val(row_sums, col_sums, diag_sums)
    # who needs to get to goal


if __name__ == '__main__':
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    formingMagicSquare(s)
