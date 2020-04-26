import os
from typing import Dict, Sequence

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

example = (
    "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
)


def grid_values(grid: str = example) -> Dict[str, str]:
    """
    Take in a string of values representing each box in the sudoku problem and
    assign each value to a box key in the dictionary
    """
    dots_removed = [i if i is not "." else cols for i in grid]
    return {box: val for box, val in zip(boxes, dots_removed)}


def display(grid_values: dict):
    """
    NOTE: Taken directly from the solution set
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1 + max(len(grid_values[s]) for s in boxes)
    line = "+".join(["-" * (width * 3)] * 3)
    for r in rows:
        print(
            "".join(
                grid_values[r + c].center(width) + ("|" if c in "36" else "")
                for c in cols
            )
        )
        if r in "CF":
            print(line)
    return


print("\nProblem Set:\n")
display(grid_values())
