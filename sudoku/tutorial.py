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

# A mapping of box -> units
units = {s: [u for u in unitlist if s in u] for s in boxes}

# A mapping of box -> peers
peers = {s: set(sum(units[s], [])) - set(s) for s in boxes}

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


def eliminate(grid_values: dict) -> Dict[str, str]:
    solved = [box for box in grid_values.keys() if len(grid_values[box]) == 1]
    for box in solved:
        digit = grid_values[box]
        for peer in peers[box]:
            grid_values[peer] = grid_values[peer].replace(digit, "")

    return grid_values


def only_choice(grid_values: dict) -> Dict[str, str]:
    for unit in unitlist:
        for digit in "123456789":
            dplaces = [box for box in unit if digit in grid_values[box]]
            if len(dplaces) == 1:
                grid_values[dplaces[0]] = digit

    return grid_values


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len(
            [box for box in values.keys() if len(values[box]) == 1]
        )
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len(
            [box for box in values.keys() if len(values[box]) == 1]
        )
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


print(reduce_puzzle(grid_values()))
