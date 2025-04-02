# Algorithms in Python

This repository contains a collection of algorithms implemented in Python, serving as a model of examples for study and reference.

## Available Algorithms

### 1. Binary Search
Binary search is an efficient algorithm for finding an element in a sorted list. It works by repeatedly dividing the list in half, reducing the search space by half with each iteration.

#### Implementation

```python
def binary_search(lst, element):
    start, end = 0, len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if lst[mid] == element:
            return mid  # Element found
        elif lst[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1  # Element not found

# Usage example
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
search_element = 7
result = binary_search(sorted_list, search_element)
print(f"Element found at position: {result}")
```

#### Complexity
- **Best case**: O(1) - When the element is found in the middle of the list on the first attempt.
- **Worst case**: O(log n) - When the element is at the end or not present in the list.

## How to Contribute
If you want to add new algorithms, follow these steps:
1. Fork the repository.
2. Create a new Python file with your algorithm.
3. Document the implementation in `README.md`.
4. Submit a Pull Request.

## License
This project is under the MIT license. Feel free to use and modify it.

