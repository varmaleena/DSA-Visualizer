import os
import sys
import time
import random
import streamlit as st

# Correctly calculate and add project root to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))  # app/pages
project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))  # dsa_hub root
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Debug print (visible in terminal; remove after testing)
print(f"Added to sys.path: {project_root}")

# Define Frame class (assuming it's not defined or missing attributes in core.models.frame)
class Frame:
    def __init__(self, step, view, narration, data, metrics, highlights):
        self.step = step
        self.view = view
        self.narration = narration
        self.data = data
        self.metrics = metrics
        self.highlights = highlights

st.set_page_config(page_title="Sorting Forest", layout="wide")

# Data for all sorting algorithms (GFG-style info)
sorting_algorithms = {
    "Insertion Sort": {
        "description": """
- **Insertion Sort**: Builds a sorted array one item at a time, like sorting playing cards. Efficient for small or nearly sorted datasets.
- **Use Cases**: Small lists, online sorting where data arrives incrementally.
        """,
        "complexity": """
- **Time Complexity**: O(n²) worst/average case, O(n) best case.  
- **Space Complexity**: O(1) (in-place).  
- **Stable**: Yes.
        """,
        "code": {
            "Python": """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # [5, 6, 11, 12, 13]
            """,
            "Java": """
void insertionSort(int arr[]) {
    int n = arr.length;
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Example
int arr[] = {12, 11, 13, 5, 6};
insertionSort(arr);
            """,
            "C++": """
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Example
int arr[] = {12, 11, 13, 5, 6};
int n = sizeof(arr)/sizeof(arr[0]);
insertionSort(arr, n);
            """
        },
        "problems": [
            {"title": "Sort an Array", "url": "https://leetcode.com/problems/sort-an-array/"},
            {"title": "Insertion Sort List", "url": "https://leetcode.com/problems/insertion-sort-list/"},
            {"title": "Sort Array By Parity", "url": "https://leetcode.com/problems/sort-array-by-parity/"}
        ],
        "resources": [
            {"title": "GFG: Insertion Sort", "url": "https://www.geeksforgeeks.org/insertion-sort/"}
        ]
    },
    "Bubble Sort": {
        "description": """
- **Bubble Sort**: Repeatedly swaps adjacent elements if they are in the wrong order. Simple but inefficient for large lists.
- **Use Cases**: Educational purposes, small datasets.
        """,
        "complexity": """
- **Time Complexity**: O(n²) worst/best/average case.  
- **Space Complexity**: O(1).  
- **Stable**: Yes.
        """,
        "code": {
            "Python": """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
arr = [64, 34, 25, 12, 22]
print(bubble_sort(arr))  # [12, 22, 25, 34, 64]
            """,
            "Java": """
void bubbleSort(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}
            """,
            "C++": """
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}
            """
        },
        "problems": [
            {"title": "Sort Colors", "url": "https://leetcode.com/problems/sort-colors/"},
            {"title": "Sort List", "url": "https://leetcode.com/problems/sort-list/"}
        ],
        "resources": [
            {"title": "GFG: Bubble Sort", "url": "https://www.geeksforgeeks.org/bubble-sort/"}
        ]
    },
    "Selection Sort": {
        "description": """
- **Selection Sort**: Finds the minimum element in the unsorted part and swaps it with the first unsorted element.
- **Use Cases**: Small lists, when minimizing swaps is important.
        """,
        "complexity": """
- **Time Complexity**: O(n²) all cases.  
- **Space Complexity**: O(1).  
- **Stable**: No.
        """,
        "code": {
            "Python": """
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
            """,
            "Java": """
void selectionSort(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
            """,
            "C++": """
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}
            """
        },
        "problems": [
            {"title": "Sort an Array", "url": "https://leetcode.com/problems/sort-an-array/"},
            {"title": "Kth Largest Element in an Array", "url": "https://leetcode.com/problems/kth-largest-element-in-an-array/"}
        ],
        "resources": [
            {"title": "GFG: Selection Sort", "url": "https://www.geeksforgeeks.org/selection-sort/"}
        ]
    },
    "Merge Sort": {
        "description": """
- **Merge Sort**: Divide-and-conquer algorithm that splits the array, sorts halves, and merges them.
- **Use Cases**: Large datasets, external sorting.
        """,
        "complexity": """
- **Time Complexity**: O(n log n) all cases.  
- **Space Complexity**: O(n).  
- **Stable**: Yes.
        """,
        "code": {
            "Python": """
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)  # [5, 6, 7, 11, 12, 13]
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/"},
            {"title": "Sort an Array", "url": "https://leetcode.com/problems/sort-an-array/"}
        ],
        "resources": [
            {"title": "GFG: Merge Sort", "url": "https://www.geeksforgeeks.org/merge-sort/"}
        ]
    },
    "Quick Sort": {
        "description": """
- **Quick Sort**: Divide-and-conquer algorithm that picks a pivot and partitions the array around it.
- **Use Cases**: General-purpose sorting, efficient on average.
        """,
        "complexity": """
- **Time Complexity**: O(n log n) average, O(n²) worst case.  
- **Space Complexity**: O(log n).  
- **Stable**: No.
        """,
        "code": {
            "Python": """
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [1, 5, 7, 8, 9, 10]
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Kth Largest Element in an Array", "url": "https://leetcode.com/problems/kth-largest-element-in-an-array/"},
            {"title": "Sort an Array", "url": "https://leetcode.com/problems/sort-an-array/"}
        ],
        "resources": [
            {"title": "GFG: Quick Sort", "url": "https://www.geeksforgeeks.org/quick-sort/"}
        ]
    },
    "Heap Sort": {
        "description": """
- **Heap Sort**: Builds a max-heap and repeatedly extracts the maximum element.
- **Use Cases**: When O(n log n) time is needed with O(1) space.
        """,
        "complexity": """
- **Time Complexity**: O(n log n) all cases.  
- **Space Complexity**: O(1).  
- **Stable**: No.
        """,
        "code": {
            "Python": """
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # [5, 6, 7, 11, 12, 13]
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Kth Largest Element in an Array", "url": "https://leetcode.com/problems/kth-largest-element-in-an-array/"},
            {"title": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/"}
        ],
        "resources": [
            {"title": "GFG: Heap Sort", "url": "https://www.geeksforgeeks.org/heap-sort/"}
        ]
    },
    "Counting Sort": {
        "description": """
- **Counting Sort**: Counts occurrences of each value and reconstructs the sorted array. Non-comparison based.
- **Use Cases**: When values are in a limited range (e.g., integers 0-100).
        """,
        "complexity": """
- **Time Complexity**: O(n + k) where k is the range.  
- **Space Complexity**: O(k).  
- **Stable**: Yes.
        """,
        "code": {
            "Python": """
def counting_sort(arr):
    max_val = max(arr) if arr else 0
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    output = []
    for i, c in enumerate(count):
        output.extend([i] * c)
    return output

# Example
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))  # [1, 2, 2, 3, 3, 4, 8]
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Sort Characters By Frequency", "url": "https://leetcode.com/problems/sort-characters-by-frequency/"},
            {"title": "Sort Array by Increasing Frequency", "url": "https://leetcode.com/problems/sort-array-by-increasing-frequency/"}
        ],
        "resources": [
            {"title": "GFG: Counting Sort", "url": "https://www.geeksforgeeks.org/counting-sort/"}
        ]
    },
    "Radix Sort": {
        "description": """
- **Radix Sort**: Sorts integers by grouping by individual digits (using Counting Sort as subroutine).
- **Use Cases**: Sorting large numbers or strings.
        """,
        "complexity": """
- **Time Complexity**: O(d(n + k)) where d is digits, k is base.  
- **Space Complexity**: O(n + k).  
- **Stable**: Yes.
        """,
        "code": {
            "Python": """
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

# Example
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # [2, 24, 45, 66, 75, 90, 170, 802]
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Sort Characters By Frequency", "url": "https://leetcode.com/problems/sort-characters-by-frequency/"},
            {"title": "Maximum Gap", "url": "https://leetcode.com/problems/maximum-gap/"}
        ],
        "resources": [
            {"title": "GFG: Radix Sort", "url": "https://www.geeksforgeeks.org/radix-sort/"}
        ]
    }
}

# ------------------------------------------------------
# Helper: Create frames for visualization
# ------------------------------------------------------
def _yield_array(step, array, desc, variables=None, stats=None, highlights=None):
    return Frame(
        step=step,
        view=array[:],
        narration=desc,
        data=variables or {},
        metrics=stats or {},
        highlights=highlights or {},
    )

# ------------------------------------------------------
# Insertion Sort
# ------------------------------------------------------
def insertion_sort_frames(arr):
    a = arr[:]
    step = 0
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        yield _yield_array(step, a, f"Consider element {key} at index {i}",
                           {"i": i, "j": j}, {}, {"compare": [i]})
        step += 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            yield _yield_array(step, a, f"Shift {a[j]} to the right",
                               {"i": i, "j": j}, {"comparisons": 1, "swaps": 1},
                               {"swap": [j, j+1]})
            step += 1
            j -= 1
        a[j + 1] = key
        yield _yield_array(step, a, f"Insert {key} at position {j+1}",
                           {"i": i, "j": j}, {"swaps": 1}, {"swap": [j+1]})
        step += 1

# ------------------------------------------------------
# Bubble Sort
# ------------------------------------------------------
def bubble_sort_frames(arr):
    a = arr[:]
    step = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield _yield_array(step, a, f"Compare {a[j]} and {a[j+1]}",
                               {"i": i, "j": j}, {"comparisons": 1},
                               {"compare": [j, j+1]})
            step += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield _yield_array(step, a, f"Swap {a[j]} and {a[j+1]}",
                                   {"i": i, "j": j}, {"swaps": 1},
                                   {"swap": [j, j+1]})
                step += 1

# ------------------------------------------------------
# Selection Sort
# ------------------------------------------------------
def selection_sort_frames(arr):
    a = arr[:]
    step = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield _yield_array(step, a, f"Compare {a[min_idx]} and {a[j]}",
                               {"i": i, "j": j}, {"comparisons": 1},
                               {"compare": [min_idx, j]})
            step += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        yield _yield_array(step, a, f"Swap {a[i]} and {a[min_idx]}",
                           {"i": i, "min_idx": min_idx}, {"swaps": 1},
                           {"swap": [i, min_idx]})
        step += 1

# ------------------------------------------------------
# Merge Sort
# ------------------------------------------------------
def merge_sort_frames(arr):
    a = arr[:]
    step = 0

    def merge_sort(l, r):
        nonlocal step
        if l < r:
            m = (l + r) // 2
            yield from merge_sort(l, m)
            yield from merge_sort(m + 1, r)
            yield from merge(l, m, r)

    def merge(l, m, r):
        nonlocal step
        left = a[l:m+1]
        right = a[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            yield _yield_array(step, a, f"Compare {left[i]} and {right[j]}",
                               {"i": i, "j": j}, {"comparisons": 1},
                               {"compare": [l+i, m+1+j]})
            step += 1
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            yield _yield_array(step, a, f"Insert {a[k]} at index {k}",
                               {"k": k}, {"swaps": 1}, {"swap": [k]})
            step += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            yield _yield_array(step, a, f"Insert {a[k]} from left",
                               {"k": k}, {"swaps": 1}, {"swap": [k]})
            step += 1
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            yield _yield_array(step, a, f"Insert {a[k]} from right",
                               {"k": k}, {"swaps": 1}, {"swap": [k]})
            step += 1
            j += 1
            k += 1

    yield from merge_sort(0, len(a) - 1)

# ------------------------------------------------------
# Quick Sort
# ------------------------------------------------------
def quick_sort_frames(arr, pivot_strategy="last"):
    a = arr[:]
    step = 0

    def quick_sort(low, high):
        nonlocal step
        if low < high:
            pi = partition(low, high)
            yield from quick_sort(low, pi - 1)
            yield from quick_sort(pi + 1, high)

    def choose_pivot(low, high):
        if pivot_strategy == "first":
            return low
        elif pivot_strategy == "median3":
            mid = (low + high) // 2
            trio = [(a[low], low), (a[mid], mid), (a[high], high)]
            trio.sort(key=lambda x: x[0])
            return trio[1][1]
        elif pivot_strategy == "random":
            return random.randint(low, high)
        else:
            return high

    def partition(low, high):
        nonlocal step
        pivot_idx = choose_pivot(low, high)
        a[pivot_idx], a[high] = a[high], a[pivot_idx]
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            yield _yield_array(step, a, f"Compare {a[j]} with pivot {pivot}",
                               {"j": j, "pivot": pivot}, {"comparisons": 1},
                               {"compare": [j], "pivot": [high]})
            step += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                yield _yield_array(step, a, f"Swap {a[i]} and {a[j]}",
                                   {"i": i, "j": j}, {"swaps": 1},
                                   {"swap": [i, j], "pivot": [high]})
                step += 1
        a[i + 1], a[high] = a[high], a[i + 1]
        yield _yield_array(step, a, f"Place pivot {pivot} at position {i+1}",
                           {"pivot": pivot}, {"swaps": 1},
                           {"swap": [i+1], "pivot": [i+1]})
        step += 1
        return i + 1

    yield from quick_sort(0, len(a) - 1)

# ------------------------------------------------------
# Heap Sort
# ------------------------------------------------------
def heap_sort_frames(arr):
    a = arr[:]
    step = 0
    n = len(a)

    def heapify(n, i):
        nonlocal step
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            yield _yield_array(step, a, f"Swap {a[i]} and {a[largest]}",
                               {"i": i, "largest": largest}, {"swaps": 1},
                               {"swap": [i, largest]})
            step += 1
            yield from heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        yield _yield_array(step, a, f"Swap root {a[i]} with {a[0]}",
                           {"i": i}, {"swaps": 1}, {"swap": [0, i]})
        step += 1
        yield from heapify(i, 0)

# ------------------------------------------------------
# Counting Sort
# ------------------------------------------------------
def counting_sort_frames(arr):
    a = arr[:]
    step = 0
    max_val = max(a) if a else 0
    count = [0] * (max_val + 1)
    for num in a:
        count[num] += 1
        yield _yield_array(step, a, f"Count occurrence of {num}",
                           {"num": num}, {"updates": 1}, {"compare": [a.index(num)]})
        step += 1
    output = []
    for i, c in enumerate(count):
        for _ in range(c):
            output.append(i)
            yield _yield_array(step, output + a[len(output):],
                               f"Place {i} into output", {"i": i}, {"writes": 1},
                               {"swap": [len(output)-1]})
            step += 1
    a[:] = output
    yield _yield_array(step, a, "Final sorted array", {}, {}, {})

# ------------------------------------------------------
# Radix Sort
# ------------------------------------------------------
def radix_sort_frames(arr):
    a = arr[:]
    step = 0

    def counting_sort_exp(exp):
        nonlocal step
        n = len(a)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (a[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (a[i] // exp) % 10
            output[count[index] - 1] = a[i]
            count[index] -= 1
            yield _yield_array(step, output + a[len(output):],
                               f"Place {a[i]} at position {count[index]}",
                               {"exp": exp}, {}, {"swap": [count[index]]})
            step += 1
            i -= 1
        for i in range(n):
            a[i] = output[i]
            yield _yield_array(step, a, f"Write back {a[i]}",
                               {"exp": exp}, {}, {"swap": [i]})
            step += 1

    max_val = max(a) if a else 0
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_exp(exp)
        exp *= 10

# Render array function (matching searching style)
def render_array(array, title="Array", highlights=None):
    colors = ["#222428"] * len(array)  # Default dark color
    if highlights:
        # Color for swap (teal)
        for idx in highlights.get("swap", []):
            if 0 <= idx < len(colors):
                colors[idx] = "#00BFAE"
        # Color for compare (yellow, if not swap)
        for idx in highlights.get("compare", []):
            if 0 <= idx < len(colors) and colors[idx] == "#222428":
                colors[idx] = "#FFD600"
        # Color for pivot (red)
        for idx in highlights.get("pivot", []):
            if 0 <= idx < len(colors):
                colors[idx] = "#FF5252"
    
    html = "".join(
        f"<span style='display:inline-block;width:40px;height:40px;"
        f"border-radius:10px;margin:4px;background:{c};color:#fff;line-height:40px;text-align:center;'>{v}</span>"
        for v, c in zip(array, colors)
    )
    st.subheader(title)
    st.markdown(html, unsafe_allow_html=True)

# ===== DYNAMIC INFO BAR (Updates based on selected algorithm) =====
selected_algo = st.selectbox("Algorithm", list(sorting_algorithms.keys()), index=0)

with st.expander(f"ℹ️ {selected_algo}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    algo_data = sorting_algorithms[selected_algo]
    
    st.markdown("### Overview")
    st.markdown(algo_data["description"])
    
    st.markdown("### Complexity")
    st.markdown(algo_data["complexity"])
    
    st.markdown("### Code Snippet")
    language = st.selectbox("Language", ["Python", "Java", "C++"], key="code_lang")
    st.code(algo_data["code"][language], language=language.lower())
    
    st.markdown("### Top-Rated LeetCode Problems")
    for prob in algo_data["problems"]:
        st.markdown(f"- [{prob['title']}]({prob['url']})")
    
    st.markdown("### Additional Resources")
    for res in algo_data["resources"]:
        st.markdown(f"- [{res['title']}]({res['url']})")

# Session state for playback
if "frames" not in st.session_state:
    st.session_state.frames = []
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "playing" not in st.session_state:
    st.session_state.playing = False

# Inputs
st.title("Sorting Forest")
st.caption("Experiment with arrays and watch sorting algorithms step by step.")

array_input = st.text_input("Array (comma-separated integers)", value="5,3,4,1,2,7,8,9")
try:
    input_arr = [int(x.strip()) for x in array_input.split(",") if x.strip()]
except ValueError:
    st.error("Invalid array input. Use comma-separated integers.")
    st.stop()

speed = st.slider("Speed (steps/sec)", 1, 10, 5)

# Controls
c1, c2, c3, c4, c5 = st.columns(5)
generate_clicked = c1.button("Generate", key="btn_generate")
play_clicked = c2.button("Play", key="btn_play")
pause_clicked = c3.button("Pause", key="btn_pause")
step_clicked = c4.button("Step", key="btn_step")
reset_clicked = c5.button("Reset", key="btn_reset")

# Function to generate frames based on selected algo
def generate_frames(arr, algo):
    if algo == "Insertion Sort":
        return list(insertion_sort_frames(arr))
    elif algo == "Bubble Sort":
        return list(bubble_sort_frames(arr))
    elif algo == "Selection Sort":
        return list(selection_sort_frames(arr))
    elif algo == "Merge Sort":
        return list(merge_sort_frames(arr))
    elif algo == "Quick Sort":
        return list(quick_sort_frames(arr))
    elif algo == "Heap Sort":
        return list(heap_sort_frames(arr))
    elif algo == "Counting Sort":
        return list(counting_sort_frames(arr))
    elif algo == "Radix Sort":
        return list(radix_sort_frames(arr))
    return []

# Generate button logic
if generate_clicked:
    st.session_state.frames = generate_frames(input_arr, selected_algo)
    st.session_state.idx = 0
    st.session_state.playing = False
    st.success("Frames generated!")

# Play, Pause, Step, Reset logic
if play_clicked:
    st.session_state.playing = True

if pause_clicked:
    st.session_state.playing = False

if step_clicked:
    if st.session_state.frames and st.session_state.idx < len(st.session_state.frames) - 1:
        st.session_state.idx += 1
    st.rerun()

if reset_clicked:
    st.session_state.idx = 0
    st.session_state.playing = False
    st.rerun()

# Display
left, right = st.columns([3, 2])

def render_current():
    if not st.session_state.frames:
        st.info("Enter an array, choose an algorithm, and click Generate to create frames.")
        return
    frame = st.session_state.frames[st.session_state.idx]
    with left:
        render_array(frame.view, title=f"Array — Step {frame.step}", highlights=frame.highlights)
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
        
    st.caption(f"Frame {st.session_state.idx + 1} / {len(st.session_state.frames)}")

# Animation loop
if st.session_state.playing and st.session_state.frames:
    render_current()
    if st.session_state.idx < len(st.session_state.frames) - 1:
        st.session_state.idx += 1
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.playing = False
        st.rerun()
else:
    render_current()

st.markdown("---")
st.caption("Tip: Experiment with different arrays and algorithms to see the steps.")
