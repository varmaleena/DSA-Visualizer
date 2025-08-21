import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


import time
import streamlit as st
from core.models.frame import Frame
from core.views.stack_queue_view import render_stack, render_queue
from core.algorithms.stack_queue import (
    stack_push_frames,
    stack_pop_frames,
    queue_enqueue_frames,
    queue_dequeue_frames,
)


st.set_page_config(page_title="Stack & Queue ", layout="wide")


# Data for Stack and Queue (GFG-style info)
structures_info = {
    "Stack": {
        "description": """
- **Stack**: A linear data structure following LIFO (Last In, First Out) principle. Elements are added/removed from the top.
- **Use Cases**: Function call recursion, undo/redo features, expression evaluation (e.g., postfix).
        """,
        "complexity": """
- **Push/Pop Time**: O(1) (amortized for dynamic arrays).  
- **Space Complexity**: O(n) for n elements.  
- **Operations**: Push (add to top), Pop (remove from top), Peek (view top).
        """,
        "code": {
            "Python": """
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

# Example
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # 20
            """,
            "Java": """
import java.util.Stack;

Stack<Integer> stack = new Stack<>();
stack.push(10);
stack.push(20);
System.out.println(stack.pop());  // 20
            """,
            "C++": """
#include <stack>

std::stack<int> stack;
stack.push(10);
stack.push(20);
std::cout << stack.top() << std::endl;  // 20
stack.pop();
            """
        },
        "problems": [
            {"title": "Valid Parentheses", "url": "https://leetcode.com/problems/valid-parentheses/"},
            {"title": "Next Greater Element I", "url": "https://leetcode.com/problems/next-greater-element-i/"},
            {"title": "Min Stack", "url": "https://leetcode.com/problems/min-stack/"}
        ],
        "resources": [
            {"title": "GFG: Stack Data Structure", "url": "https://www.geeksforgeeks.org/stack-data-structure/"},
            {"title": "Visualgo: Stack", "url": "https://visualgo.net/en/stack"}
        ]
    },
    "Queue": {
        "description": """
- **Queue**: A linear data structure following FIFO (First In, First Out) principle. Elements are added at rear and removed from front.
- **Use Cases**: Task scheduling, breadth-first search (BFS), buffering (e.g., print queues).
        """,
        "complexity": """
- **Enqueue/Dequeue Time**: O(1) (with linked list or circular buffer).  
- **Space Complexity**: O(n) for n elements.  
- **Operations**: Enqueue (add to rear), Dequeue (remove from front), Peek (view front).
        """,
        "code": {
            "Python": """
from collections import deque

queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
print(queue.popleft())  # Dequeue: 10
            """,
            "Java": """
import java.util.Queue;
import java.util.LinkedList;

Queue<Integer> queue = new LinkedList<>();
queue.add(10);  // Enqueue
queue.add(20);
System.out.println(queue.poll());  // Dequeue: 10
            """,
            "C++": """
#include <queue>

std::queue<int> queue;
queue.push(10);  // Enqueue
queue.push(20);
std::cout << queue.front() << std::endl;  // 10
queue.pop();  // Dequeue
            """
        },
        "problems": [
            {"title": "Implement Stack using Queues", "url": "https://leetcode.com/problems/implement-stack-using-queues/"},
            {"title": "Sliding Window Maximum", "url": "https://leetcode.com/problems/sliding-window-maximum/"},
            {"title": "Number of Recent Calls", "url": "https://leetcode.com/problems/number-of-recent-calls/"}
        ],
        "resources": [
            {"title": "GFG: Queue Data Structure", "url": "https://www.geeksforgeeks.org/queue-data-structure/"},
            {"title": "Visualgo: Queue", "url": "https://visualgo.net/en/queue"}
        ]
    }
}

st.title("Stack & Queue Hangar")
st.caption("Practice LIFO and FIFO operations with step-by-step visuals.")


# ===== DYNAMIC INFO BAR (Updates based on selected structure) =====
selected_structure = st.selectbox("Structure", list(structures_info.keys()), index=0)

with st.expander(f"ℹ️ {selected_structure}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    structure_data = structures_info[selected_structure]
    
    st.markdown("### Overview")
    st.markdown(structure_data["description"])
    
    st.markdown("### Complexity")
    st.markdown(structure_data["complexity"])
    
    st.markdown("### Code Snippet")
    language = st.selectbox("Language", ["Python", "Java", "C++"], key="code_lang")
    st.code(structure_data["code"][language], language=language.lower())
    
    st.markdown("### Top-Rated LeetCode Problems")
    for prob in structure_data["problems"]:
        st.markdown(f"- [{prob['title']}]({prob['url']})")
    
    st.markdown("### Additional Resources")
    for res in structure_data["resources"]:
        st.markdown(f"- [{res['title']}]({res['url']})")


# Session state
if "sq_frames" not in st.session_state:
    st.session_state.sq_frames = []
if "sq_idx" not in st.session_state:
    st.session_state.sq_idx = 0
if "sq_playing" not in st.session_state:
    st.session_state.sq_playing = False


# Inputs
default_vals = "2,4,6" if selected_structure == "Stack" else "10,20,30"
vals_text = st.text_input("Initial values (comma-separated)", default_vals)
try:
    values = [int(x.strip()) for x in vals_text.split(",") if x.strip() != ""]
except ValueError:
    values = [x.strip() for x in vals_text.split(",") if x.strip() != ""]


if selected_structure == "Stack":
    op = st.selectbox("Operation", ["Push", "Pop"])
else:
    op = st.selectbox("Operation", ["Enqueue", "Dequeue"])


x_input_needed = (selected_structure == "Stack" and op == "Push") or (selected_structure == "Queue" and op == "Enqueue")
val = None
if x_input_needed:
    x_text = st.text_input("Value to add", "9" if selected_structure == "Stack" else "40")
    try:
        val = int(x_text)
    except ValueError:
        val = x_text


speed = st.slider("Speed (steps/sec)", 1, 10, 5)


# Controls
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("Generate"):
    if selected_structure == "Stack":
        if op == "Push":
            st.session_state.sq_frames = list(stack_push_frames(values, val))
        else:
            st.session_state.sq_frames = list(stack_pop_frames(values))
    else:
        if op == "Enqueue":
            st.session_state.sq_frames = list(queue_enqueue_frames(values, val))
        else:
            st.session_state.sq_frames = list(queue_dequeue_frames(values))
    st.session_state.sq_idx = 0
    st.session_state.sq_playing = False


if c2.button("Play"):
    st.session_state.sq_playing = True
if c3.button("Pause"):
    st.session_state.sq_playing = False
if c4.button("Step"):
    if st.session_state.sq_frames:
        st.session_state.sq_idx = min(st.session_state.sq_idx + 1, len(st.session_state.sq_frames) - 1)
if c5.button("Restart"):
    st.session_state.sq_idx = 0
    st.session_state.sq_playing = False


# Display
left, right = st.columns([3, 2])


def render_current():
    if not st.session_state.sq_frames:
        st.info("Enter values, choose an operation, then click Generate.")
        return
    frame: Frame = st.session_state.sq_frames[st.session_state.sq_idx]
    with left:
        if selected_structure == "Stack":
            render_stack(frame.view, title=f"Stack — Step {frame.step}")
        else:
            render_queue(frame.view, title=f"Queue — Step {frame.step}")
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
    st.caption(f"Frame {st.session_state.sq_idx + 1} / {len(st.session_state.sq_frames)}")


# Animation loop
if st.session_state.sq_playing and st.session_state.sq_frames:
    render_current()
    if st.session_state.sq_idx < len(st.session_state.sq_frames) - 1:
        st.session_state.sq_idx += 1
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.sq_playing = False
        st.rerun()
else:
    render_current()


st.markdown("---")
st.caption("Highlights: Stack top (blue), current (yellow), moved (red). Queue front (blue), rear (green), current (yellow), moved (red).")
