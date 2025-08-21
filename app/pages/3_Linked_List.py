import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import time
import streamlit as st
from core.models.frame import Frame
from core.views.list_view import render_linked_list
from core.algorithms.linked_list import SinglyLinkedList, DoublyLinkedList, CircularLinkedList

st.set_page_config(page_title="Linked List ", layout="wide")

# Data for all linked list types (GFG-style info)
linked_list_types_info = {
    "Singly Linked List": {
        "description": """
- **Singly Linked List**: A linear collection of nodes where each node points to the next (one-way links).
- **Use Cases**: Stacks, queues, simple dynamic lists; memory-efficient for insertions/deletions at ends.
        """,
        "complexity": """
- **Insert/Search/Delete Time**: O(n) worst case (traverse from head).  
- **Space Complexity**: O(n) for n nodes (one pointer per node).  
- **Direction**: Forward only.
        """,
        "code": {
            "Python": """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

# Example
sll = SinglyLinkedList()
sll.insert_head(10)
sll.insert_head(5)
            """,
            "Java": """
class Node {
    int value;
    Node next;
    Node(int value) { this.value = value; }
}

class SinglyLinkedList {
    Node head;

    void insertHead(int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }
}
            """,
            "C++": """
struct Node {
    int value;
    Node* next;
    Node(int val) : value(val), next(nullptr) {}
};

class SinglyLinkedList {
public:
    Node* head = nullptr;

    void insertHead(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }
};
            """
        },
        "problems": [
            {"title": "Merge Two Sorted Lists", "url": "https://leetcode.com/problems/merge-two-sorted-lists/"},
            {"title": "Remove Duplicates from Sorted List", "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/"},
            {"title": "Linked List Cycle", "url": "https://leetcode.com/problems/linked-list-cycle/"}
        ],
        "resources": [
            {"title": "GFG: Singly Linked List", "url": "https://www.geeksforgeeks.org/introduction-to-linked-list-data-structure/"},
            {"title": "Visualgo: Linked List", "url": "https://visualgo.net/en/list"}
        ]
    },
    "Doubly Linked List": {
        "description": """
- **Doubly Linked List**: Each node has pointers to both next and previous nodes (two-way links).
- **Use Cases**: Browsers (back/forward navigation), undo/redo functionality; efficient bidirectional traversal.
        """,
        "complexity": """
- **Insert/Search/Delete Time**: O(n) worst case, but faster deletions with prev pointers.  
- **Space Complexity**: O(n) (two pointers per node).  
- **Direction**: Bidirectional.
        """,
        "code": {
            "Python": """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

# Example
dll = DoublyLinkedList()
dll.insert_head(10)
dll.insert_head(5)
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Design Linked List", "url": "https://leetcode.com/problems/design-linked-list/"},
            {"title": "Flatten a Multilevel Doubly Linked List", "url": "https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/"}
        ],
        "resources": [
            {"title": "GFG: Doubly Linked List", "url": "https://www.geeksforgeeks.org/doubly-linked-list/"}
        ]
    },
    "Circular Linked List": {
        "description": """
- **Circular Linked List**: Like singly/doubly, but the last node points back to the first (forms a circle).
- **Use Cases**: Round-robin scheduling, multiplayer games (cycling turns); no null end.
        """,
        "complexity": """
- **Insert/Search/Delete Time**: O(n) worst case; careful with cycles to avoid infinite loops.  
- **Space Complexity**: O(n).  
- **Direction**: Forward (singly circular) or bidirectional (doubly circular).
        """,
        "code": {
            "Python": """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

# Example
cll = CircularLinkedList()
cll.insert_head(10)
cll.insert_head(5)
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Linked List Cycle II", "url": "https://leetcode.com/problems/linked-list-cycle-ii/"},
            {"title": "Insert into a Sorted Circular Linked List", "url": "https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/"}
        ],
        "resources": [
            {"title": "GFG: Circular Linked List", "url": "https://www.geeksforgeeks.org/circular-linked-list/"}
        ]
    }
}

# ===== DYNAMIC INFO BAR (Updates based on selected list type) =====
selected_list_type = st.selectbox("Linked List Type", list(linked_list_types_info.keys()), index=0)

with st.expander(f"ℹ️ {selected_list_type}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    list_data = linked_list_types_info[selected_list_type]
    
    st.markdown("### Overview")
    st.markdown(list_data["description"])
    
    st.markdown("### Complexity")
    st.markdown(list_data["complexity"])
    
    st.markdown("### Code Snippet")
    language = st.selectbox("Language", ["Python", "Java", "C++"], key="code_lang")
    st.code(list_data["code"][language], language=language.lower())
    
    st.markdown("### Top-Rated LeetCode Problems")
    for prob in list_data["problems"]:
        st.markdown(f"- [{prob['title']}]({prob['url']})")
    
    st.markdown("### Additional Resources")
    for res in list_data["resources"]:
        st.markdown(f"- [{res['title']}]({res['url']})")

st.title("Linked List Lab")
st.caption("Visualize linked list operations step-by-step.")

# Session state for playback
if "ll_frames" not in st.session_state:
    st.session_state.ll_frames = []
if "ll_idx" not in st.session_state:
    st.session_state.ll_idx = 0
if "ll_playing" not in st.session_state:
    st.session_state.ll_playing = False

# Inputs
list_text = st.text_input("List values (comma-separated)", "1,3,5,7")
try:
    values = [int(x.strip()) for x in list_text.split(",") if x.strip() != ""]
except ValueError:
    values = [x.strip() for x in list_text.split(",") if x.strip() != ""]

op = st.selectbox("Operation", ["Insert Head", "Insert Tail", "Search", "Delete Value"])

x = st.text_input("Value (for insert/search/delete)", "4")
try:
    val = int(x)
except ValueError:
    val = x

speed = st.slider("Speed (steps/sec)", 1, 10, 5)

# Controls
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("Generate"):
    if selected_list_type == "Singly Linked List":
        ll = SinglyLinkedList()
    elif selected_list_type == "Doubly Linked List":
        ll = DoublyLinkedList()
    elif selected_list_type == "Circular Linked List":
        ll = CircularLinkedList()
    else:
        st.error("Invalid list type.")
        st.stop()

    # Build initial list by consuming the generators to perform insertions
    for v in values:
        for _ in ll.insert_tail_frames(v):
            pass  # Consume generator to execute insertion

    if op == "Insert Head":
        st.session_state.ll_frames = list(ll.insert_head_frames(val))
    elif op == "Insert Tail":
        st.session_state.ll_frames = list(ll.insert_tail_frames(val))
    elif op == "Search":
        st.session_state.ll_frames = list(ll.search_frames(val))
    elif op == "Delete Value":
        st.session_state.ll_frames = list(ll.delete_value_frames(val))
    st.session_state.ll_idx = 0
    st.session_state.ll_playing = False

if c2.button("Play"):
    st.session_state.ll_playing = True
if c3.button("Pause"):
    st.session_state.ll_playing = False
if c4.button("Step"):
    if st.session_state.ll_frames:
        st.session_state.ll_idx = min(st.session_state.ll_idx + 1, len(st.session_state.ll_frames) - 1)
if c5.button("Restart"):
    st.session_state.ll_idx = 0
    st.session_state.ll_playing = False

# Display
left, right = st.columns([3, 2])

def render_current():
    if not st.session_state.ll_frames:
        st.info("Enter values, choose an operation, then click Generate.")
        return
    frame: Frame = st.session_state.ll_frames[st.session_state.ll_idx]
    with left:
        render_linked_list(frame.view, title=f"Linked List — Step {frame.step}")
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
        
    st.caption(f"Frame {st.session_state.ll_idx + 1} / {len(st.session_state.ll_frames)}")

# Animation loop
if st.session_state.ll_playing and st.session_state.ll_frames:
    render_current()
    if st.session_state.ll_idx < len(st.session_state.ll_frames) - 1:
        st.session_state.ll_idx += 1
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.ll_playing = False
        st.rerun()
else:
    render_current()

st.markdown("---")
st.caption("Highlights: head (blue), tail (red), current (yellow), prev (light-blue), found (green).")
