import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import time
import streamlit as st
from core.models.frame import Frame
from core.views.array_view import render_array
from core.algorithms.searching import (
    linear_search_frames,
    binary_search_frames,
    rotated_binary_search_frames,
)

st.set_page_config(page_title="Searching ", layout="wide")

# Data for all searching algorithms (GFG-style info)
searching_algorithms = {
    "Linear Search": {
        "description": """
- **Linear Search**: Sequentially checks each element until a match is found or the end is reached.
- **Use Cases**: Unsorted arrays, small datasets, or when simplicity is key.
        """,
        "complexity": """
- **Time Complexity**: O(n) worst/average case, O(1) best case.  
- **Space Complexity**: O(1).  
- **Requires Sorted Array**: No.
        """,
        "code": {
            "Python": """
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [1, 3, 4, 7, 9, 12, 15]
print(linear_search(arr, 7))  # 3
            """,
            "Java": """
int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
            """,
            "C++": """
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
            """
        },
        "problems": [
            {"title": "Find Minimum in Rotated Sorted Array", "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"},
            {"title": "Search Insert Position", "url": "https://leetcode.com/problems/search-insert-position/"}
        ],
        "resources": [
            {"title": "GFG: Linear Search", "url": "https://www.geeksforgeeks.org/linear-search/"}
        ]
    },
    "Binary Search (sorted)": {
        "description": """
- **Binary Search**: Efficiently finds a target in a sorted array by repeatedly dividing the search interval in half.
- **Use Cases**: Large sorted datasets, dictionaries, phone books.
        """,
        "complexity": """
- **Time Complexity**: O(log n).  
- **Space Complexity**: O(1).  
- **Requires Sorted Array**: Yes.
        """,
        "code": {
            "Python": """
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [1, 3, 4, 7, 9, 12, 15]
print(binary_search(arr, 7))  # 3
            """,
            "Java": """
int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
            """,
            "C++": """
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
            """
        },
        "problems": [
            {"title": "Binary Search", "url": "https://leetcode.com/problems/binary-search/"},
            {"title": "Search in Rotated Sorted Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
            {"title": "Find Peak Element", "url": "https://leetcode.com/problems/find-peak-element/"}
        ],
        "resources": [
            {"title": "GFG: Binary Search", "url": "https://www.geeksforgeeks.org/binary-search/"},
            {"title": "Visualgo: Binary Search", "url": "https://visualgo.net/en/binsearch"}
        ]
    },
    "Rotated Binary Search": {
        "description": """
- **Rotated Binary Search**: Variant of binary search for sorted arrays rotated at some pivot (e.g., [4,5,6,7,0,1,2]).
- **Use Cases**: Searching in rotated logs or arrays where rotation point is unknown.
        """,
        "complexity": """
- **Time Complexity**: O(log n).  
- **Space Complexity**: O(1).  
- **Requires Sorted Array**: Yes (rotated sorted).
        """,
        "code": {
            "Python": """
def rotated_binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:  # Left half sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Example
arr = [9, 12, 15, 1, 3, 4, 7]
print(rotated_binary_search(arr, 4))  # 5
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Search in Rotated Sorted Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
            {"title": "Find Minimum in Rotated Sorted Array", "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"}
        ],
        "resources": [
            {"title": "GFG: Search in Rotated Array", "url": "https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/"}
        ]
    }
}

st.title("Searching Grounds")
st.caption("Watch search ranges shrink and decisions unfold step-by-step.")

# ===== DYNAMIC INFO BAR (Updates based on selected algorithm) =====
selected_algo = st.selectbox("Algorithm", list(searching_algorithms.keys()), index=0)

with st.expander(f"ℹ️ {selected_algo}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    algo_data = searching_algorithms[selected_algo]
    
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
if "frames_s" not in st.session_state:
    st.session_state.frames_s = []
if "idx_s" not in st.session_state:
    st.session_state.idx_s = 0
if "playing_s" not in st.session_state:
    st.session_state.playing_s = False

# Inputs
arr_text = st.text_input("Array (integers, comma-separated)", "1,3,4,7,9,12,15")
try:
    arr = [int(x.strip()) for x in arr_text.split(",") if x.strip() != ""]
except ValueError:
    st.error("Please enter valid integers separated by commas.")
    st.stop()

target = st.number_input("Target", value=7, step=1)

if selected_algo == "Binary Search (sorted)":
    if arr != sorted(arr):
        st.warning("Array is not sorted—binary search may not work correctly.")
elif selected_algo == "Rotated Binary Search":
    st.info("Use a rotated sorted array (e.g., 9,12,15,1,3,4,7).")

speed = st.slider("Speed (steps/sec)", 1, 10, 5)

# Controls
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("Generate"):
    try:
        if selected_algo == "Linear Search":
            st.session_state.frames_s = list(linear_search_frames(arr, int(target)))
        elif selected_algo == "Binary Search (sorted)":
            st.session_state.frames_s = list(binary_search_frames(arr, int(target)))
        elif selected_algo == "Rotated Binary Search":
            st.session_state.frames_s = list(rotated_binary_search_frames(arr, int(target)))
        st.session_state.idx_s = 0
        st.session_state.playing_s = False
    except Exception as e:
        st.error(f"Error generating frames: {str(e)}")

if c2.button("Play"):
    st.session_state.playing_s = True

if c3.button("Pause"):
    st.session_state.playing_s = False

if c4.button("Step"):
    if st.session_state.frames_s:
        st.session_state.idx_s = min(st.session_state.idx_s + 1, len(st.session_state.frames_s) - 1)

if c5.button("Restart"):
    st.session_state.idx_s = 0
    st.session_state.playing_s = False

# Display
left, right = st.columns([3, 2])

def render_current():
    if not st.session_state.frames_s:
        st.info("Enter the array/target, choose an algorithm, then click Generate.")
        return
    frame: Frame = st.session_state.frames_s[st.session_state.idx_s]
    with left:
        render_array(frame.view, title=f"Array — Step {frame.step}")
        # Highlight legend
        
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
        
    st.caption(f"Frame {st.session_state.idx_s + 1} / {len(st.session_state.frames_s)}")

# Animation loop with progress bar
progress_bar = st.progress(0)
if st.session_state.playing_s and st.session_state.frames_s:
    render_current()
    if st.session_state.idx_s < len(st.session_state.frames_s) - 1:
        st.session_state.idx_s += 1
        progress_bar.progress((st.session_state.idx_s + 1) / len(st.session_state.frames_s))
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.playing_s = False
        progress_bar.empty()
        st.rerun()
else:
    render_current()
    if st.session_state.frames_s:
        progress_bar.progress((st.session_state.idx_s + 1) / len(st.session_state.frames_s))

st.markdown("---")
st.caption("Tip: Use a sorted array for Binary Search; try a rotated array like 9,12,15,1,3,4,7 for the rotated variant.")
