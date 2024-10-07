def linear_search(arr: list, target: int) -> int:
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage
arr = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(arr, target)

if result != -1:
    print(f"Element was found at index: {result}")
else:
    print("Element was not found in the array")
