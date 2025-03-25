def native_search(l, target):
    """Simple linear search (O(n) complexity)"""
    for i in range(len(l)):  # Fixed loop range
        if l[i] == target:
            return i
    return -1  # Return -1 if target not found

def binary_search(l, target, low=None, high=None):
    """Binary search (O(log n) complexity) - Recursive"""
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1  # Fix: Subtract 1 for correct index range

    if low > high:  # Base case: target not found
        return -1

    midpoint = (low + high) // 2  # Correct midpoint calculation

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)  # Search left half
    else:
        return binary_search(l, target, midpoint + 1, high)  # Search right half

# Example usage:
l = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

print(f"Native Search Index: {native_search(l, target)}")  # Output: 3
print(f"Binary Search Index: {binary_search(l, target)}")  # Output: 3
