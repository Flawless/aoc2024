# day3_tasks.py
import re
from common import fetch_puzzle_input


def parse_puzzle_input(puzzle_input):
    # Extract all valid mul(X, Y), do(), and don't() instructions using regex
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))"
    matches = re.findall(pattern, puzzle_input)

    instructions = []
    enabled = True  # Initially, mul instructions are enabled

    # Process each instruction match
    for match in matches:
        instruction = match[0]
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul") and enabled:
            x, y = int(match[1]), int(match[2])
            instructions.append((x, y))

    return instructions


def calculate_total_product(instructions):
    # Calculate the sum of all products from the valid instructions
    total_product = sum(x * y for x, y in instructions)
    return total_product


def main():
    # Fixed day number for the puzzle
    day_number = 3

    # Fetch the puzzle input for the given day
    puzzle_input = fetch_puzzle_input(day_number)
    print("Puzzle input fetched successfully.")

    # Parse the input into valid mul instructions
    instructions = parse_puzzle_input(puzzle_input)

    # Calculate and print the total product of all valid mul instructions
    total_product = calculate_total_product(instructions)
    print(f"Total product: {total_product}")


if __name__ == "__main__":
    main()
