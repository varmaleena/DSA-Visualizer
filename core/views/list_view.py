from typing import Dict, Any, List
import streamlit as st

def render_linked_list(view: Dict[str, Any], title: str = "Linked List"):
    values: List[Any] = view.get("values", [])
    highlights: Dict[str, Any] = view.get("highlights", {})

    st.subheader(title)
    if not values:
        st.info("List is empty.")
        return

    # Highlights: current (yellow), prev (light blue), head (blue), tail (red), found (green)
    def style_for(i: int) -> str:
        if "found" in highlights and highlights["found"] is not None and i == highlights["found"]:
            return "background:#06d6a0;color:white;"
        if "current" in highlights and highlights["current"] is not None and i == highlights["current"]:
            return "background:#ffd166;"
        if "prev" in highlights and highlights["prev"] is not None and i == highlights["prev"]:
            return "background:#a8dadc;"
        if "head" in highlights and highlights["head"] is not None and i == highlights["head"]:
            return "background:#118ab2;color:white;"
        if "tail" in highlights and highlights["tail"] is not None and i == highlights["tail"]:
            return "background:#ef476f;color:white;"
        return ""

    cols = st.columns(len(values) * 2 - 1) if len(values) > 1 else st.columns(1)
    c_idx = 0
    for i, v in enumerate(values):
        box_style = style_for(i)
        cols[c_idx].markdown(
            f"<div style='text-align:center;padding:10px;{box_style};"
            f"border:1px solid #ddd;border-radius:6px;min-width:60px'>{v}</div>",
            unsafe_allow_html=True
        )
        c_idx += 1
        if i != len(values) - 1:
            cols[c_idx].markdown("<div style='text-align:center;padding:10px'>→</div>", unsafe_allow_html=True)
            c_idx += 1
