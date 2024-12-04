from common import fetch_puzzle_input

day_number = 4
puzzle_input = fetch_puzzle_input(day_number)


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            # Check if the current cell contains 'A', which is the center of the X-MAS pattern
            if grid[i][j] == "A":
                # Check Diagonal 1 (from top-left to bottom-right)
                valid_diag1 = False
                if (
                    0 <= i - 1 < rows
                    and 0 <= j - 1 < cols
                    and 0 <= i + 1 < rows
                    and 0 <= j + 1 < cols
                ):
                    diag1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
                    if diag1 == "MAS" or diag1 == "SAM":
                        valid_diag1 = True

                # Check Diagonal 2 (from top-right to bottom-left)
                valid_diag2 = False
                if (
                    0 <= i - 1 < rows
                    and 0 <= j + 1 < cols
                    and 0 <= i + 1 < rows
                    and 0 <= j - 1 < cols
                ):
                    diag2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
                    if diag2 == "MAS" or diag2 == "SAM":
                        valid_diag2 = True

                # If both diagonals are valid, we have found an X-MAS
                if valid_diag1 and valid_diag2:
                    count += 1

    return count


def main():
    # Process the puzzle input into a grid (list of lists)
    grid = [
        list(line.strip()) for line in puzzle_input.strip().split("\n") if line.strip()
    ]
    result = count_x_mas(grid)
    print(f"The number of X-MAS occurrences is: {result}")


if __name__ == "__main__":
    main()
