import os
from typing import Dict, Sequence


example = (
    "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
)


class Sudoku(object):
    def __init__(self, sequence: str = example):
        # Inputs for problem definiton
        self.solved = False
        self.stalled = False
        self.counter = 1
        self.sequence = sequence
        self.rows = "ABCDEFGHI"
        self.cols = "123456789"

        # Boxes and units definition
        self.boxes = self.cross(self.rows, self.cols)
        self.row_units = [self.cross(r, self.cols) for r in self.rows]
        self.col_units = [self.cross(self.rows, c) for c in self.cols]
        self.square_units = [
            self.cross(rs, cs)
            for rs in ("ABC", "DEF", "GHI")
            for cs in ("123", "456", "789")
        ]
        self.unitlist = self.row_units + self.col_units + self.square_units

        # Box dictionaries
        self.units_for_box = {
            box: [unit for unit in self.unitlist if box in unit] for box in self.boxes
        }
        self.peers_for_box = {
            box: set(sum(self.units_for_box[box], [])) - {box} for box in self.boxes
        }

        # Initialize grid_values
        self.init_grid_values()
        self.display()

    def cross(self, a: str, b: str) -> Sequence[str]:
        return [s + t for s in a for t in b]

    def init_grid_values(self) -> Dict[str, str]:
        """
        """
        dots_replaced_with_digits = [
            digit if digit is not "." else self.cols for digit in self.sequence
        ]

        self.grid_values = {
            box: digits for box, digits in zip(self.boxes, dots_replaced_with_digits)
        }
        self.is_solved()
        return self.grid_values

    def solved_boxes(self):
        return [box for box in self.boxes if len(self.grid_values[box]) == 1]

    def is_solved(self):
        if len(self.solved_boxes()) == len(self.boxes):
            self.solved = True
            return True

        self.boxes_remaining = len(self.boxes) - len(self.solved_boxes())
        return False

    def display(self):
        """
        NOTE: Taken directly from the solution set
        Display the values as a 2-D grid.
        Input: The sudoku in dictionary form
        Output: None
        """
        if not self.solved:
            print(f"\nStep {self.counter}: {self.boxes_remaining} unsolved boxes!\n")
        else:
            print(f"\nStep {self.counter}: Solution found!\n")
        width = 1 + max(len(self.grid_values[box]) for box in self.boxes)
        line = "+".join(["-" * (width * 3)] * 3)
        for r in self.rows:
            print(
                "".join(
                    self.grid_values[r + c].center(width) + ("|" if c in "36" else "")
                    for c in self.cols
                )
            )
            if r in "CF":
                print(line)
        return

    def eliminate(self):
        """
        """
        self.counter += 1
        solved_boxes = self.solved_boxes()
        for box in solved_boxes:
            solved_digit = self.grid_values[box]
            for peer in self.peers_for_box[box]:
                self.grid_values[peer] = self.grid_values[peer].replace(
                    solved_digit, ""
                )
        self.is_solved()
        self.display()

    def only_choice(self):
        """
        """
        self.counter += 1
        for unit in self.unitlist:
            for digit in self.cols:
                options = [box for box in unit if digit in self.grid_values[box]]
                if len(options) == 1:
                    self.grid_values[options[0]] = digit
        self.is_solved()
        self.display()

    def take_step(self):
        solved_boxes_before = len(self.solved_boxes())
        self.eliminate()
        self.only_choice()
        solved_boxes_after = len(self.solved_boxes())

        if solved_boxes_after == solved_boxes_before:
            self.stalled = True
            print("\n---- No Solution Found ----\n")

    def solve(self):
        while not self.stalled:
            if self.solved:
                break

            self.take_step()


sudoku = Sudoku()
sudoku.solve()
