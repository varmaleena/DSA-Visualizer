# core/views/graph_view.py (Updated to Handle Unweighted Graphs Safely)
from typing import Dict, List, Tuple
import streamlit as st

def render_graph(view: Dict[int, List[Tuple[int, int]]], title: str = "Graph City", highlights: Dict[int, str] = {}):
    nodes = list(view.keys())
    st.subheader(title)
    if not nodes:
        st.info("Graph is empty.")
        return

    # Simple text-based node-link render with highlights (boxes for nodes, arrows for edges)
    cols = st.columns(len(nodes))
    color_map = {
        "green": "#06d6a0",  # Visited
        "yellow": "#ffd166", # Current
        "red": "#ef476f",    # Updated
    }

    for i, node in enumerate(nodes):
        bg_color = "#1E1E1E"
        text_color = "white"
        if node in highlights:
            color = highlights[node]
            bg_color = color_map.get(color, "#FFD700")
            text_color = "black" if color == "yellow" else "white"

        cols[i].markdown(
            f"""
            <div style='background-color:{bg_color}; color:{text_color}; padding:12px; border-radius:8px; border:1px solid #444; text-align:center; font-weight:bold;'>{node}</div>
            """,
            unsafe_allow_html=True,
        )

    # Display edges below (simple text) with safe unpacking
    st.write("Edges:")
    for u in view:
        neighbors = view[u]
        for neighbor in neighbors:
            if isinstance(neighbor, tuple):
                v, w = neighbor
            else:
                v = neighbor  # Unweighted: assume int is neighbor, default weight 1
                w = 1
            st.write(f"{u} → {v} (weight: {w})")

# Test (optional)
if __name__ == "__main__":
    test_graph = {0: [1, 2], 1: [3], 2: [], 3: []}  # unweighted (ints)
    render_graph(test_graph, highlights={0: "yellow", 1: "green"})
