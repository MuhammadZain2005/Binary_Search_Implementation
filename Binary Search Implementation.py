"""
BINARY SEARCH

Difficulty: 1/10

Comments: Had to revise binary search
"""


import time

def binary_search(lst, target, find_first=True):
    low = 0
    high = len(lst) - 1
    result = -1
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            result = mid
            if find_first:
                high = mid - 1
            else:
                low = mid + 1
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    end_time = time.time()
    time_taken = end_time - start_time
    return result, time_taken

def find_all_occurrences(lst, target):
    first_index, _ = binary_search(lst, target, find_first=True)
    if first_index == -1:
        return []

    last_index, _ = binary_search(lst, target, find_first=False)

    return list(range(first_index, last_index + 1))

# Test cases
result, time_taken = binary_search([1, 2, 3, 4, 5, 6, 7], 4)
print(f"Single Occurrence: Index={result}, Time Taken={time_taken:.6f} seconds")

result, time_taken = binary_search([1, 2, 3, 4, 5, 6, 7], 8)
print(f"Not Found: Index={result}, Time Taken={time_taken:.6f} seconds")

result, time_taken = binary_search([1, 2, 3, 4, 4, 4, 5], 4)
print(f"First Occurrence: Index={result}, Time Taken={time_taken:.6f} seconds")

result, time_taken = binary_search([1, 2, 3, 4, 4, 4, 5], 4, find_first=False)
print(f"Last Occurrence: Index={result}, Time Taken={time_taken:.6f} seconds")

all_occurrences = find_all_occurrences([1, 2, 3, 4, 4, 4, 5], 4)
print(f"All Occurrences: Indices={all_occurrences}")
