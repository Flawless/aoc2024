import os
import requests
from collections import Counter

SESSION_TOKEN = os.getenv("SESSION_TOKEN")
URL = "https://adventofcode.com/2024/day/1/input"


def fetch_puzzle_input(url, session_token):
    headers = {"Cookie": f"session={session_token}", "User-Agent": "Python script"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error if the request failed
    return response.text


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


# Fetch the puzzle input
try:
    puzzle_input = fetch_puzzle_input(URL, SESSION_TOKEN)
    print("Puzzle input fetched successfully.")
except requests.RequestException as e:
    print(f"Error fetching input: {e}")
    exit(1)

# Parse the input into left and right lists
left_list, right_list = parse_puzzle_input(puzzle_input)

# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")

# Calculate and print the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {similarity_score}")
