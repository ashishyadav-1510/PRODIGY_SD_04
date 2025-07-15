# 🧩 Sudoku Solver (Python)

A fully interactive and beginner-friendly Python program to **solve 9x9 Sudoku puzzles** using the  **Backtracking Algorithm** . This project demonstrates recursion, validation, file handling, and clean console output formatting.

## ✅ Features

* Accepts 9x9 Sudoku input with support for empty cells (denoted by `0`)
* Automatically validates the initial puzzle for correctness
* Solves the puzzle using an optimized **recursive backtracking algorithm**
* Nicely formats the grid with 3x3 section dividers
* Saves both the original puzzle and its solution to `.txt` files
* Modular, clean, and beginner-friendly structure

## 🧠 How It Works

### 1. User Input

* The program prompts the user to enter **9 rows** of numbers.
* Each row must contain **exactly 9 integers** separated by spaces.
* Use `0` for  **empty cells** .

Row 1: 5 3 0 0 7 0 0 0 0
Row 2: 6 0 0 1 9 5 0 0 0
...
If the input is invalid, the program asks again until it receives a valid row.

### 2. Puzzle Validation

Before solving, the program checks whether the initial puzzle violates any **Sudoku rules** (no duplicates in rows, columns, or 3x3 subgrids).
If the puzzle is invalid, the program halts with a warning.

### 3. Backtracking Algorithm

The solving logic uses  **recursion + backtracking** :

| Step                | Logic                                                  |
| ------------------- | ------------------------------------------------------ |
| Find empty cell     | Traverse the grid to locate a zero (empty cell)        |
| Try placing numbers | Try values from 1 to 9                                 |
| Check for validity  | Ensure the number doesn't violate Sudoku rules         |
| Recurse             | Proceed to the next empty cell recursively             |
| Backtrack if needed | If stuck, reset cell to 0 and try next possible number |

---

### 4. File Saving

After solving:

* The original input puzzle is saved as `sudoku_input.txt`
* The final solution (along with original) is saved to a file of your choice

PUZZLE
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
...

SOLUTION OF PUZZLE
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
...

## 📌 Code Overview

Core Methods:

def input_from_user(self):
    # Reads 9 rows of input and validates the format

def is_valid(self, row, col, num):
    # Checks whether placing a number is valid

def is_valid_puzzle(self):
    # Ensures the original puzzle follows Sudoku rules

def solve(self):
    # Backtracking algorithm to fill empty cells

def save_to_file(self, filename, heading, include_original=False):
    # Saves the puzzle and/or solution to a .txt file

## 📸 Screenshots

## Code:

![image](https://github.com/ashishyadav-1510/PRODIGY_SD_04/blob/main/screenshot/Screenshot%202025-07-15%20151557.png?raw=true)
![image](https://github.com/ashishyadav-1510/PRODIGY_SD_04/blob/main/screenshot/Screenshot%202025-07-15%20151636.png?raw=true)

## Output:

![image](https://github.com/ashishyadav-1510/PRODIGY_SD_04/blob/main/screenshot/Screenshot%202025-07-15%20152021.png?raw=true)

### Sample of input.txt

![image](https://github.com/ashishyadav-1510/PRODIGY_SD_04/blob/main/screenshot/Screenshot%202025-07-15%20152038.png?raw=true)

### Sample of output.txt

![image](https://github.com/ashishyadav-1510/PRODIGY_SD_04/blob/main/screenshot/Screenshot%202025-07-15%20152055.png?raw=true)

## Video:

[Video on YouTube](https://youtu.be/wnSwHG921c8?si=MLrVg2ZdbkX8bKnB)

## Explanation

🔷 Class Definition
class SudokuSolver:
Declares a class named SudokuSolver.
A class is a blueprint for creating objects and encapsulating related data and functions.

🔷 Constructor Method: __init__
def __init__(self):
    self.grid = []
    self.original_grid = []
The constructor is called when an object of SudokuSolver is created.
self.grid: To store the working copy of the Sudoku board (9x9 matrix).
self.original_grid: To store the original puzzle (before solving).

🔷 Input Method: input_from_user
def input_from_user(self):
    print("Enter Sudoku Puzzle row by row :")
Prompts the user to enter the puzzle row by row (9 rows).

    for i in range(9):
        while True:
Loops through 9 rows (Sudoku grid is 9x9).
while True: Keeps asking until valid input is entered.

            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
Takes user input (space-separated), converts each value to integer, and stores it as a list called row.

                if len(row) != 9 or not all(0 <= num <= 9 for num in row):
                    raise ValueError
Validates: Row must contain exactly 9 numbers between 0 and 9 (0 = empty cell).

                self.grid.append(row)
                break
Adds the valid row to self.grid.
break: exits the while loop after successful entry.

            except ValueError:
                print("Invalid input.\nEnter exactly 9 numbers between 0 to 9!!")
If input is invalid, error message is shown and re-prompts the user.

    self.original_grid = [row[:] for row in self.grid]
Creates a deep copy of the input grid for backup (original_grid).

🔷 Saving to File: save_to_file
def save_to_file(self, filename, heading, include_original=False):
Saves Sudoku puzzle or solution to a text file.
Parameters: filename (file name), heading (title for section), include_original (bool to include puzzle).

    try:
        with open(filename, 'w') as file:
Tries to open file in write mode ('w') to overwrite content.

            if include_original:
                self._write_grid(file, self.original_grid, "PUZZLE")
                file.write("\n")
If include_original is True, writes the original puzzle to the file.

            self._write_grid(file, self.grid, heading)
Writes the current grid (solution) with the given heading.

    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")
Handles file I/O errors and prints the reason.

🔷 Grid Writer Helper: _write_grid
def _write_grid(self, file_obj, grid, title):
Writes a formatted Sudoku grid to a file or console.
Parameters: file object, grid to write, and title.

    file_obj.write(f"{title}\n")
Writes the section title.

    for i in range(9):
        if i % 3 == 0 and i != 0:
            file_obj.write("-" * 21 + "\n")
Adds horizontal separator after every 3 rows (for 3x3 box visual separation).

        for j in range(9):
            if j % 3 == 0 and j != 0:
                file_obj.write("| ")
Adds vertical separator after every 3 columns.

            cell = str(grid[i][j]) if grid[i][j] != 0 else "."
            file_obj.write(cell + " ")
Converts 0 to "." for clarity (empty cell), writes cell value followed by a space.

        file_obj.write("\n")
Moves to next row after each row is printed.

🔷 Grid Printer: print_grid
def print_grid(self, grid=None):
    if grid is None:
        grid = self.grid
If no grid is passed, it defaults to the current self.grid.

    print("\nSolved Sudoku:")
    self._write_grid(file_obj=__import__('sys').stdout, grid=grid, title="")
Uses sys.stdout to write directly to console.
Calls _write_grid to print the grid.

🔷 Validation: is_valid
def is_valid(self, row, col, num):
Checks if placing num at (row, col) is valid.

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
Computes starting index of the 3x3 subgrid that the cell belongs to.

    for i in range(9):
        if self.grid[row][i] == num or self.grid[i][col] == num:
            return False
Checks if num exists in the same row or column → return False if found.

    return all(self.grid[box_row + i // 3][box_col + i % 3] != num for i in range(9))
Checks the 3x3 box for duplicates of num using a single loop.

🔷 Puzzle Validity Check: is_valid_puzzle
def is_valid_puzzle(self):
Ensures the initial puzzle doesn't break Sudoku rules.

    for row in range(9):
        for col in range(9):
            num = self.grid[row][col]
Iterates over each cell.

            if num != 0:
                self.grid[row][col] = 0
Temporarily sets current cell to 0 to test validity without self-checking.

                if not self.is_valid(row, col, num):
                    self.grid[row][col] = num
                    return False
                self.grid[row][col] = num
If placing that number again is invalid → puzzle is invalid.

    return True
If all cells are valid → returns True.

🔷 Backtracking Solver: solve
def solve(self):
    for row in range(9):
        for col in range(9):
            if self.grid[row][col] == 0:
Finds the next empty cell (0).

                for num in range(1, 10):
                    if self.is_valid(row, col, num):
                        self.grid[row][col] = num
Tries placing numbers 1 through 9.
Places a number if it's valid.

                        if self.solve():
                            return True
                        self.grid[row][col] = 0
Recursively tries to solve the rest.
If it fails, resets the cell and backtracks.

                return False
    return True
If no empty cell is found, returns True → puzzle is solved.

🔷 Main Program Execution
if __name__ == "__main__":
Ensures the following code runs only when the file is executed directly, not when imported.

    solver = SudokuSolver()
Creates an instance of SudokuSolver.

    print("*** SUDUKO SOLVER ***\n(use 0 for empty cells\nuse space for separation of each number)")
    solver.input_from_user()
Displays usage instructions.
Takes puzzle input.

    solver.save_to_file("sudoku_input.txt", heading="PUZZLE")
Saves the initial puzzle to a file.

    if not solver.is_valid_puzzle():
        print("The input puzzle is invalid. Please correct it.")
        exit()
Checks if the input puzzle is valid.
If not valid, exits the program.

    if solver.solve():
        solver.print_grid()
Solves the puzzle using backtracking.
Prints the solution if successful.

        output_filename = input("Enter output filename( with .txt extension): ").strip()
        if not output_filename.endswith(".txt"):
            output_filename += ".txt"
Prompts user to enter filename for saving output.
Appends .txt if not included.

        solver.save_to_file(output_filename, heading="SOLUTION OF PUZZLE", include_original=True)
        print(f"Puzzle and solution saved to '{output_filename}'")
Saves both puzzle and solution to the specified file.

    else:
        print("No solution exists for the given puzzle.")
If puzzle is unsolvable, notifies the user.

## Author
***Ashish Yadav***