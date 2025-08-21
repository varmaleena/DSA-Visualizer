import os
import sys
import time
import streamlit as st


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from core.algorithms.trees import BST, AVL, MinHeap, MaxHeap
from core.views.tree_view import render_tree_array


st.set_page_config(page_title="Trees ", layout="wide")


# Data for all tree types (GFG-style info)
tree_types_info = {
    "BST": {
        "description": """
- **Binary Search Tree (BST)**: A binary tree where for each node, all elements in its left subtree are less than the node, and all in the right are greater.
- **Use Cases**: Efficient searching, insertion, and deletion in sorted data; basis for more advanced structures.
        """,
        "complexity": """
- **Insert/Search/Delete Time**: O(h) average (h = height, O(log n) balanced, O(n) worst skewed).  
- **Space Complexity**: O(n) for n nodes.  
- **Balanced**: No (can become skewed).
        """,
        "code": {
            "Python": """
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break

# Example
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
            """,
            "Java": """
class Node {
    int value;
    Node left, right;
    Node(int value) {
        this.value = value;
        left = right = null;
    }
}

class BST {
    Node root;

    void insert(int value) {
        root = insertRec(root, value);
    }

    Node insertRec(Node root, int value) {
        if (root == null) {
            root = new Node(value);
            return root;
        }
        if (value < root.value)
            root.left = insertRec(root.left, value);
        else if (value > root.value)
            root.right = insertRec(root.right, value);
        return root;
    }
}
            """,
            "C++": """
struct Node {
    int value;
    Node* left;
    Node* right;
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BST {
public:
    Node* root = nullptr;

    void insert(int value) {
        root = insertRec(root, value);
    }

    Node* insertRec(Node* root, int value) {
        if (root == nullptr)
            return new Node(value);
        if (value < root->value)
            root->left = insertRec(root->left, value);
        else if (value > root->value)
            root->right = insertRec(root->right, value);
        return root;
    }
};
            """
        },
        "problems": [
            {"title": "Validate Binary Search Tree", "url": "https://leetcode.com/problems/validate-binary-search-tree/"},
            {"title": "Insert into a Binary Search Tree", "url": "https://leetcode.com/problems/insert-into-a-binary-search-tree/"},
            {"title": "Kth Smallest Element in a BST", "url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/"}
        ],
        "resources": [
            {"title": "GFG: Binary Search Tree", "url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/"},
            {"title": "Visualgo: BST", "url": "https://visualgo.net/en/bst"}
        ]
    },
    "AVL": {
        "description": """
- **AVL Tree**: A self-balancing BST where the height difference between left and right subtrees is at most 1, ensuring O(log n) operations.
- **Use Cases**: When frequent insertions/deletions require balanced trees for performance.
        """,
        "complexity": """
- **Insert/Search/Delete Time**: O(log n).  
- **Space Complexity**: O(n).  
- **Balanced**: Yes (via rotations).
        """,
        "code": {
            "Python": """
# Refer to GFG for full AVL insert with rotations.
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Balance a Binary Search Tree", "url": "https://leetcode.com/problems/balance-a-binary-search-tree/"},
            {"title": "Convert Sorted Array to Binary Search Tree", "url": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"}
        ],
        "resources": [
            {"title": "GFG: AVL Tree", "url": "https://www.geeksforgeeks.org/avl-tree-set-1-insertion/"}
        ]
    },
    "Min Heap": {
        "description": """
- **Min Heap**: A complete binary tree where each node is smaller than its children; root is the minimum.
- **Use Cases**: Priority queues, Dijkstra's algorithm, heap sort.
        """,
        "complexity": """
- **Insert/Extract Min Time**: O(log n).  
- **Space Complexity**: O(n).  
- **Balanced**: Yes (complete tree).
        """,
        "code": {
            "Python": """
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

# Example
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Kth Largest Element in a Stream", "url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/"},
            {"title": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/"}
        ],
        "resources": [
            {"title": "GFG: Binary Heap", "url": "https://www.geeksforgeeks.org/binary-heap/"}
        ]
    },
    "Max Heap": {
        "description": """
- **Max Heap**: A complete binary tree where each node is larger than its children; root is the maximum.
- **Use Cases**: Heap sort (descending), priority queues for max priority.
        """,
        "complexity": """
- **Insert/Extract Max Time**: O(log n).  
- **Space Complexity**: O(n).  
- **Balanced**: Yes (complete tree).
        """,
        "code": {
            "Python": """
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

# Example
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(15)
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Kth Smallest Element in a Sorted Matrix", "url": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/"},
            {"title": "Find Median from Data Stream", "url": "https://leetcode.com/problems/find-median-from-data-stream/"}
        ],
        "resources": [
            {"title": "GFG: Binary Heap", "url": "https://www.geeksforgeeks.org/binary-heap/"}
        ]
    }
}

# ===== DYNAMIC INFO BAR (Updates based on selected tree type) =====
selected_tree_type = st.selectbox("Tree Type", list(tree_types_info.keys()), index=0)  # All tree types visible

with st.expander(f"ℹ️ {selected_tree_type}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    tree_data = tree_types_info[selected_tree_type]
    
    st.markdown("### Overview")
    st.markdown(tree_data["description"])
    
    st.markdown("### Complexity")
    st.markdown(tree_data["complexity"])
    
    st.markdown("### Code Snippet")
    language = st.selectbox("Language", ["Python", "Java", "C++"], key="code_lang")
    st.code(tree_data["code"][language], language=language.lower())
    
    st.markdown("### Top-Rated LeetCode Problems")
    for prob in tree_data["problems"]:
        st.markdown(f"- [{prob['title']}]({prob['url']})")
    
    st.markdown("### Additional Resources")
    for res in tree_data["resources"]:
        st.markdown(f"- [{res['title']}]({res['url']})")

st.title("Trees Garden")
st.caption("Watch tree structures grow, balance, and transform step-by-step.")


# Session state
if "frames_t" not in st.session_state:
    st.session_state.frames_t = []
if "idx_t" not in st.session_state:
    st.session_state.idx_t = 0
if "playing_t" not in st.session_state:
    st.session_state.playing_t = False


# Inputs
values_text = st.text_input("Values (integers, comma-separated)", "10,5,15,3,7")
try:
    values = [int(x.strip()) for x in values_text.split(",") if x.strip() != ""]
except ValueError:
    st.error("Please enter valid integers separated by commas.")
    st.stop()


operation = st.selectbox("Operation", ["Build Tree", "Insert", "Delete"])


extra_value = None  # Initialize as None
if operation in ["Insert", "Delete"]:
    extra_value = st.number_input("Extra Value (for Insert/Delete)", value=0, step=1)
else:
    st.markdown("_Extra value disabled for Build Tree._")


speed = st.slider("Speed (steps/sec)", 1, 10, 5)


# Inline TreeGardener with step-by-step frames
class TreeGardener:
    def __init__(self, tree_type="BST"):
        if tree_type == "BST":
            self.tree = BST()
        elif tree_type == "AVL":
            self.tree = AVL()
        elif tree_type == "Min Heap":
            self.tree = MinHeap()
        elif tree_type == "Max Heap":
            self.tree = MaxHeap()
        else:
            raise ValueError("Unsupported tree type")
        self.frames = []


    def build_from_list(self, values):
        self.frames = []
        for value in values:
            # Use generator for multi-step frames per insert
            for frame in self.tree.insert_frames(value):
                self.frames.append(frame)
        return self.frames


    def perform_operation(self, operation, value):
        if operation == "insert":
            for frame in self.tree.insert_frames(value):
                self.frames.append(frame)
        elif operation == "delete":
            # Implement delete_frames similarly if needed
            pass
        return self.frames


    def get_traversal(self, traversal_type="inorder"):
        return self.tree.inorder() if traversal_type == "inorder" else []


# Controls
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("Generate"):
    gardener = TreeGardener(selected_tree_type)
    st.session_state.frames_t = []  # Reset frames


    if operation == "Build Tree":
        st.session_state.frames_t = gardener.build_from_list(values)
    elif operation == "Insert":
        if extra_value is not None:
            gardener.build_from_list(values)  # Build initial tree
            st.session_state.frames_t = gardener.perform_operation("insert", extra_value)
        else:
            st.error("Please provide an extra value for Insert.")
    elif operation == "Delete":
        if extra_value is not None:
            gardener.build_from_list(values)  # Build initial tree
            st.session_state.frames_t = gardener.perform_operation("delete", extra_value)
        else:
            st.error("Please provide an extra value for Delete.")


    st.session_state.idx_t = 0
    st.session_state.playing_t = False


if c2.button("Play"):
    st.session_state.playing_t = True


if c3.button("Pause"):
    st.session_state.playing_t = False


if c4.button("Step"):
    if st.session_state.frames_t:
        st.session_state.idx_t = min(st.session_state.idx_t + 1, len(st.session_state.frames_t) - 1)


if c5.button("Restart"):
    st.session_state.idx_t = 0
    st.session_state.playing_t = False


# Display
left, right = st.columns([3, 2])


def render_current():
    if not st.session_state.frames_t:
        st.info("Enter values, choose tree type and operation, then click Generate.")
        return
    frame = st.session_state.frames_t[st.session_state.idx_t]
    with left:
        # Fixed access: Use frame.view (assuming it's a list or dict for tree rendering)
        render_tree_array(frame.view, title=f"Tree View — Step {frame.step}")
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
        st.subheader("Metrics")
        st.json(frame.metrics)
    
    st.caption(f"Frame {st.session_state.idx_t + 1} / {len(st.session_state.frames_t)}")


# Animation loop
if st.session_state.playing_t and st.session_state.frames_t:
    render_current()
    if st.session_state.idx_t < len(st.session_state.frames_t) - 1:
        st.session_state.idx_t += 1
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.playing_t = False
        st.rerun()
else:
    render_current()


st.markdown("---")
st.caption("Tip: Start with Build Tree, then try Insert or Delete on the generated tree.")
