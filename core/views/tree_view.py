from typing import Dict, Any, List
import streamlit as st

def generate_view(root):
    """Generate a level-order list of node values for visualization. Returns [] if root is None."""
    if not root:
        return []
    from collections import deque
    view = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        view.append(node.value if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while view and view[-1] is None:
        view.pop()
    return view

def render_tree_array(view: Dict[str, Any], title: str = "Tree (Level Order)"):
    values: List[Any] = view.get("values", [])
    highlights: Dict[Any, str] = view.get("highlights", {})  # Expect {value: color_str}

    st.subheader(title)
    if not values:
        st.info("Tree is empty.")
        return

    cols = st.columns(max(1, len(values)))
    color_map = {
        "green": "#06d6a0",  # Inserted
        "red": "#ef476f",    # Deleted
        "blue": "#118ab2",   # Rotation/root
        "yellow": "#ffd166", # Current/compare
    }

    for i, v in enumerate(values):
        # Default styling
        bg_color = "#1E1E1E"
        text_color = "white"
        border_color = "#444"

        # Apply highlight if v is a key in highlights
        if v in highlights:
            color = highlights[v]
            bg_color = color_map.get(color, "#FFD700")  # Default to yellow if unknown
            text_color = "black" if color == "yellow" else "white"

        cols[i].markdown(
            f"""
            <div style='
                background-color:{bg_color};
                color:{text_color};
                padding:12px;
                border-radius:8px;
                border:1px solid {border_color};
                text-align:center;
                font-weight:bold;
            '>{v if v is not None else ''}</div>
            """,
            unsafe_allow_html=True,
        )

# Test (optional)
if __name__ == "__main__":
    test_view = {
        "values": [10, 5, 15],
        "highlights": {5: "green", 15: "red"}
    }
    render_tree_array(test_view)
