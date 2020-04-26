import os
from typing import Sequence

# Project for AIND, inspired by http://norvig.com/sudoku.html

# Individual squares at the intersection of rows and columns
# will be called 'boxes'. The complete rows, columns, and 3x3
# squares will be called 'units'. For a particular box, such as
# 'A1', its peers will be all other boxes that belong to a common
# unit, namely, those that belong to the same row, column, or 3x3


rows = "ABCDEFGHI"
cols = "123456789"


def cross(a: str, b: str) -> Sequence[str]:
    return [s + t for s in a for t in b]


# Build the board elements
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [
    cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")
]
unitlist = row_units + col_units + square_units

print("\nBoxes:\n")
print(boxes)
print("\nRow Units:\n")
print(row_units)
print("\nCol Units:\n")
print(col_units)
print("\nSquare Units:\n")
print(square_units)
