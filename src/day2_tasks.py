from common import fetch_puzzle_input


def parse_puzzle_input(puzzle_input):
    # Split the input into reports, each report is a list of integers
    reports = []
    for line in puzzle_input.strip().split("\n"):
        reports.append(list(map(int, line.split())))
    return reports


def is_safe_report(report):
    # Check if the report is either all increasing or all decreasing
    increasing = all(0 < (b - a) <= 3 for a, b in zip(report, report[1:]))
    decreasing = all(0 < (a - b) <= 3 for a, b in zip(report, report[1:]))

    return increasing or decreasing


def is_safe_with_dampener(report):
    # If the report is already safe, return True
    if is_safe_report(report):
        return True

    # Try removing each level and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe_report(modified_report):
            return True

    return False


def count_safe_reports(reports):
    # Count the number of safe reports, considering the dampener
    safe_count = sum(1 for report in reports if is_safe_with_dampener(report))
    return safe_count


def main():
    # Fixed day number for the puzzle
    day_number = 2

    # Fetch the puzzle input for the given day
    puzzle_input = fetch_puzzle_input(day_number)
    print("Puzzle input fetched successfully.")

    # Parse the input into reports
    reports = parse_puzzle_input(puzzle_input)

    # Calculate and print the number of safe reports
    safe_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_count}")


if __name__ == "__main__":
    main()
