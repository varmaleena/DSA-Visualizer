from typing import Generator, List, Dict, Any
from core.models.frame import Frame

# Helper to build highlights dict
def HL(**kwargs) -> Dict[str, Any]:
    # Only include keys that are not None
    return {k: v for k, v in kwargs.items() if v is not None}

# -------- Linear Search --------
def linear_search_frames(arr: List[int], target: int) -> Generator[Frame, None, None]:
    a = arr[:]
    step = 0
    comps = 0

    # Initial
    yield Frame(
        step=step,
        view=a,
        narration="Start Linear Search from the beginning.",
        data={"target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[0, len(a)-1] if a else [0, -1]),
    )
    step += 1

    for i, v in enumerate(a):
        comps += 1
        # Compare current index
        yield Frame(
            step=step,
            view=a,
            narration=f"Compare index {i} with target.",
            data={"i": i, "value": v, "target": target},
            metrics={"comparisons": comps},
            highlights=HL(compare=[i], range=[0, len(a)-1]),
        )
        step += 1

        if v == target:
            yield Frame(
                step=step,
                view=a,
                narration="Found target at this index.",
                data={"i": i, "value": v, "target": target},
                metrics={"comparisons": comps},
                highlights=HL(insertAt=i, range=[0, len(a)-1]),
            )
            step += 1
            return

    yield Frame(
        step=step,
        view=a,
        narration="Target not found after scanning all elements.",
        data={"target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[0, len(a)-1] if a else [0, -1]),
    )

# -------- Binary Search (sorted array) --------
def binary_search_frames(arr: List[int], target: int) -> Generator[Frame, None, None]:
    a = arr[:]  # expect sorted
    l, r = 0, len(a) - 1
    step = 0
    comps = 0

    yield Frame(
        step=step,
        view=a,
        narration="Start Binary Search on the sorted array.",
        data={"l": l, "r": r, "target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[l, r] if a else [0, -1]),
    )
    step += 1

    while l <= r:
        mid = (l + r) // 2
        comps += 1
        # Check mid
        yield Frame(
            step=step,
            view=a,
            narration=f"Check middle index {mid}.",
            data={"l": l, "r": r, "mid": mid, "target": target},
            metrics={"comparisons": comps},
            highlights=HL(range=[l, r], pivot=mid),
        )
        step += 1

        if a[mid] == target:
            yield Frame(
                step=step,
                view=a,
                narration="Found target at mid.",
                data={"l": l, "r": r, "mid": mid, "target": target},
                metrics={"comparisons": comps},
                highlights=HL(insertAt=mid, range=[l, r]),
            )
            step += 1
            return
        elif a[mid] < target:
            l = mid + 1
            yield Frame(
                step=step,
                view=a,
                narration="Target is bigger—discard left half including mid.",
                data={"l": l, "r": r, "prev_mid": mid, "target": target},
                metrics={"comparisons": comps},
                highlights=HL(range=[l, r]),
            )
            step += 1
        else:
            r = mid - 1
            yield Frame(
                step=step,
                view=a,
                narration="Target is smaller—discard right half excluding mid.",
                data={"l": l, "r": r, "prev_mid": mid, "target": target},
                metrics={"comparisons": comps},
                highlights=HL(range=[l, r]),
            )
            step += 1

    yield Frame(
        step=step,
        view=a,
        narration="Target not found.",
        data={"target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[0, len(a)-1] if a else [0, -1]),
    )

# -------- Binary Search in Rotated Sorted Array --------
def rotated_binary_search_frames(arr: List[int], target: int) -> Generator[Frame, None, None]:
    """
    Array was sorted then rotated (assume no duplicates for clarity).
    Identify sorted half each step and discard the other.
    """
    a = arr[:]
    l, r = 0, len(a) - 1
    step = 0
    comps = 0

    yield Frame(
        step=step,
        view=a,
        narration="Start search on rotated sorted array.",
        data={"l": l, "r": r, "target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[l, r] if a else [0, -1]),
    )
    step += 1

    while l <= r:
        mid = (l + r) // 2
        comps += 1
        yield Frame(
            step=step,
            view=a,
            narration=f"Check middle index {mid}.",
            data={"l": l, "r": r, "mid": mid, "target": target},
            metrics={"comparisons": comps},
            highlights=HL(range=[l, r], pivot=mid),
        )
        step += 1

        if a[mid] == target:
            yield Frame(
                step=step,
                view=a,
                narration="Found target at mid.",
                data={"l": l, "r": r, "mid": mid, "target": target},
                metrics={"comparisons": comps},
                highlights=HL(insertAt=mid, range=[l, r]),
            )
            step += 1
            return

        # Determine sorted half
        if a[l] <= a[mid]:
            # Left sorted
            yield Frame(
                step=step,
                view=a,
                narration="Left half is sorted.",
                data={"l": l, "mid": mid, "r": r, "target": target, "sorted_half": "left"},
                metrics={"comparisons": comps},
                highlights=HL(range=[l, mid]),
            )
            step += 1

            if a[l] <= target < a[mid]:
                r = mid - 1
                note = "Target in left half — move r left."
            else:
                l = mid + 1
                note = "Target not in left half — move l right."
        else:
            # Right sorted
            yield Frame(
                step=step,
                view=a,
                narration="Right half is sorted.",
                data={"l": l, "mid": mid, "r": r, "target": target, "sorted_half": "right"},
                metrics={"comparisons": comps},
                highlights=HL(range=[mid, r]),
            )
            step += 1

            if a[mid] < target <= a[r]:
                l = mid + 1
                note = "Target in right half — move l right."
            else:
                r = mid - 1
                note = "Target not in right half — move r left."

        # Updated search range
        yield Frame(
            step=step,
            view=a,
            narration=note,
            data={"l": l, "r": r, "target": target},
            metrics={"comparisons": comps},
            highlights=HL(range=[l, r]),
        )
        step += 1

    yield Frame(
        step=step,
        view=a,
        narration="Target not found.",
        data={"target": target},
        metrics={"comparisons": comps},
        highlights=HL(range=[0, len(a)-1] if a else [0, -1]),
    )
