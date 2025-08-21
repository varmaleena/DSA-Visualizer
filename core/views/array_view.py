import streamlit as st

def render_array(view, title="Array"):
    if isinstance(view, dict):
        values = view.get("values", [])
        highlights = view.get("highlights", {})
    else:
        values = list(view)
        highlights = {}

    st.subheader(title)
    cols = st.columns(len(values))
    for i, v in enumerate(values):
        # default styling
        bg_color = "#1E1E1E"  
        text_color = "white"
        border_color = "#444"  

        # highlights with defensive conversion to iterable
        compare_highlights = highlights.get("compare", [])
        if not isinstance(compare_highlights, (list, tuple)):
            compare_highlights = [compare_highlights]
        
        swap_highlights = highlights.get("swap", [])
        if not isinstance(swap_highlights, (list, tuple)):
            swap_highlights = [swap_highlights]
        
        pivot_highlights = highlights.get("pivot", [])
        if not isinstance(pivot_highlights, (list, tuple)):
            pivot_highlights = [pivot_highlights]

        if i in compare_highlights:
            bg_color = "#FFD700"
            text_color = "black"
        elif i in swap_highlights:
            bg_color = "#FF4C4C"
            text_color = "white"
        elif i in pivot_highlights:
            bg_color = "#FF8C00"
            text_color = "white"

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
            '>{v}</div>
            """,
            unsafe_allow_html=True,
        )
