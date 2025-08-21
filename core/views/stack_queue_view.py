from typing import Dict, Any, List
import streamlit as st

def render_stack(view: Dict[str, Any], title: str = "Stack"):
    values: List[Any] = view.get("values", [])
    hl: Dict[str, Any] = view.get("highlights", {})

    st.subheader(title)
    if not values:
        st.info("Stack is empty.")
        return

    # top index is highlighted
    def style_for(i: int) -> str:
        if "current" in hl and hl["current"] is not None and i == hl["current"]:
            return "background:#ffd166;"  # yellow
        if "moved" in hl and hl["moved"] is not None and i == hl["moved"]:
            return "background:#ef476f;color:white;"  # red
        if "top" in hl and hl["top"] is not None and i == hl["top"]:
            return "background:#118ab2;color:white;"  # blue
        return ""

    # Render top at the bottom for intuitive push from bottom upwards
    for i in reversed(range(len(values))):
        box_style = style_for(i)
        st.markdown(
            f"<div style='text-align:center;padding:10px;{box_style};"
            f"border:1px solid #ddd;border-radius:6px;min-width:80px;margin:6px 0'>{values[i]}</div>",
            unsafe_allow_html=True
        )

def render_queue(view: Dict[str, Any], title: str = "Queue"):
    values: List[Any] = view.get("values", [])
    hl: Dict[str, Any] = view.get("highlights", {})

    st.subheader(title)
    if not values:
        st.info("Queue is empty.")
        return

    def style_for(i: int) -> str:
        if "current" in hl and hl["current"] is not None and i == hl["current"]:
            return "background:#ffd166;"
        if "moved" in hl and hl["moved"] is not None and i == hl["moved"]:
            return "background:#ef476f;color:white;"
        if "front" in hl and hl["front"] is not None and i == hl["front"]:
            return "background:#118ab2;color:white;"
        if "rear" in hl and hl["rear"] is not None and i == hl["rear"]:
            return "background:#06d6a0;color:white;"
        return ""

    cols = st.columns(len(values))
    for i, v in enumerate(values):
        box_style = style_for(i)
        cols[i].markdown(
            f"<div style='text-align:center;padding:10px;{box_style};"
            f"border:1px solid #ddd;border-radius:6px;min-width:80px'>{v}</div>",
            unsafe_allow_html=True
        )
