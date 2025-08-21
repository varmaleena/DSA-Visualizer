from core.models.frame import Frame
import random

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
