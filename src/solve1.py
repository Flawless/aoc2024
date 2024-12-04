# day1_tasks.py
from collections import Counter
from common import fetch_puzzle_input


def parse_puzzle_input(puzzle_input):
    # Split the input into left and right lists
    left_list, right_list = [], []
    for line in puzzle_input.strip().split("\n"):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the sum of absolute differences between corresponding elements
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_counter = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(l * right_counter[l] for l in left_list)

    return similarity_score


def main():
    # Fixed day number for the puzzle
    day_number = 1

    # Fetch the puzzle input for the given day
    puzzle_input = fetch_puzzle_input(day_number)
    print("Puzzle input fetched successfully.")

    # Parse the input into left and right lists
    left_list, right_list = parse_puzzle_input(puzzle_input)

    # Calculate and print the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")

    # Calculate and print the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity score: {similarity_score}")


if __name__ == "__main__":
    main()
