from common import fetch_puzzle_input

day_number = 5
puzzle_input = fetch_puzzle_input(day_number)


def parse_input(puzzle_input):
    # Split the input into ordering rules and updates
    sections = puzzle_input.strip().split("\n\n")
    ordering_rules_section = sections[0]
    updates_section = sections[1]

    # Parse ordering rules
    ordering_rules = []
    for line in ordering_rules_section.strip().split("\n"):
        if line.strip():
            x, y = line.strip().split("|")
            ordering_rules.append((int(x), int(y)))

    # Parse updates
    updates = []
    for line in updates_section.strip().split("\n"):
        if line.strip():
            update = [int(num) for num in line.strip().split(",")]
            updates.append(update)

    return ordering_rules, updates


def is_update_correct(update, ordering_rules):
    # Build a mapping from page number to its index in the update
    page_indices = {page: idx for idx, page in enumerate(update)}

    # Filter ordering rules to those that involve pages in this update
    relevant_rules = [
        (x, y) for x, y in ordering_rules if x in page_indices and y in page_indices
    ]

    # Check each relevant ordering rule
    for x, y in relevant_rules:
        if page_indices[x] >= page_indices[y]:
            # The ordering rule is violated
            return False
    return True


def find_middle_page(update):
    # Calculate the middle index
    n = len(update)
    middle_index = n // 2
    return update[middle_index]


def topological_sort(pages, ordering_rules):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize in-degree of all pages to 0
    for page in pages:
        in_degree[page] = 0

    # Add edges and compute in-degrees
    for x, y in ordering_rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1

    # Initialize the queue with pages having in-degree 0
    queue = deque([page for page in pages if in_degree[page] == 0])

    sorted_pages = []
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_pages) != len(pages):
        # There is a cycle; cannot perform topological sort
        raise ValueError("Cannot reorder pages due to a cycle in the ordering rules.")

    return sorted_pages


def main():
    ordering_rules, updates = parse_input(puzzle_input)

    total_sum_part1 = 0
    correctly_ordered_updates = []
    incorrectly_ordered_updates = []

    # Part One: Identify correctly ordered updates
    for update in updates:
        if is_update_correct(update, ordering_rules):
            middle_page = find_middle_page(update)
            total_sum_part1 += middle_page
            correctly_ordered_updates.append((update, middle_page))
        else:
            incorrectly_ordered_updates.append(update)

    print(f"Part One: The sum of the middle page numbers is: {total_sum_part1}")

    # Part Two: Reorder incorrectly ordered updates and compute the sum
    total_sum_part2 = 0
    reordered_updates = []

    for update in incorrectly_ordered_updates:
        try:
            reordered_update = topological_sort(update, ordering_rules)
            middle_page = find_middle_page(reordered_update)
            total_sum_part2 += middle_page
            reordered_updates.append((reordered_update, middle_page))
        except ValueError as e:
            # Handle cycles if necessary
            print(f"Error reordering update {update}: {e}")

    print(
        f"Part Two: The sum of the middle page numbers after reordering is: {total_sum_part2}"
    )


if __name__ == "__main__":
    main()
