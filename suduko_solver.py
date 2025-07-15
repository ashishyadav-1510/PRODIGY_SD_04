class SudokuSolver:
    def __init__(self):
        self.grid = []
        self.original_grid = []

    def input_from_user(self):
        print("Enter Sudoku Puzzle row by row :")
        for i in range(9):
            while True:
                try:
                    row = list(map(int, input(f"Row {i + 1}: ").split()))
                    if len(row) != 9 or not all(0 <= num <= 9 for num in row):
                        raise ValueError
                    self.grid.append(row)
                    break
                except ValueError:
                    print("Invalid input.\nEnter exactly 9 numbers between 0 to 9!!")
        self.original_grid = [row[:] for row in self.grid]

    def save_to_file(self, filename, heading, include_original=False):
        try:
            with open(filename, 'w') as file:
                if include_original:
                    self._write_grid(file, self.original_grid, "PUZZLE")
                    file.write("\n")
                self._write_grid(file, self.grid, heading)
        except IOError as e:
            print(f"Error writing to file '{filename}': {e}")

    def _write_grid(self, file_obj, grid, title):
        file_obj.write(f"{title}\n")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                file_obj.write("-" * 21 + "\n")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    file_obj.write("| ")
                cell = str(grid[i][j]) if grid[i][j] != 0 else "."
                file_obj.write(cell + " ")
            file_obj.write("\n")

    def print_grid(self, grid=None):
        if grid is None:
            grid = self.grid
        print("\nSolved Sudoku:")
        self._write_grid(file_obj=__import__('sys').stdout, grid=grid, title="")

    def is_valid(self, row, col, num):
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        return all(self.grid[box_row + i // 3][box_col + i % 3] != num for i in range(9))

    def is_valid_puzzle(self):
        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]
                if num != 0:
                    self.grid[row][col] = 0
                    if not self.is_valid(row, col, num):
                        self.grid[row][col] = num
                        return False
                    self.grid[row][col] = num
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

if __name__ == "__main__":
    solver = SudokuSolver()

    print("*** SUDUKO SOLVER ***\n(use 0 for empty cells\nuse space for separation of each number)")
    solver.input_from_user()
    solver.save_to_file("sudoku_input.txt", heading="PUZZLE")

    if not solver.is_valid_puzzle():
        print("The input puzzle is invalid. Please correct it.")
        exit()

    if solver.solve():
        solver.print_grid()

        output_filename = input("Enter output filename( with .txt extension): ").strip()
        if not output_filename.endswith(".txt"):
            output_filename += ".txt"

        solver.save_to_file(output_filename, heading="SOLUTION OF PUZZLE", include_original=True)
        print(f"Puzzle and solution saved to '{output_filename}'")
    else:
        print("No solution exists for the given puzzle.")
