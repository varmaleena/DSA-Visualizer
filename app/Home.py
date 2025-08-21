import streamlit as st

st.set_page_config(page_title="DSA Learning Hub", layout="wide")

# Custom CSS (with buttons styled as cards)
st.markdown("""
    <style>
    /* Background (unchanged) */
    .stApp {
        background:
            radial-gradient(900px 700px at 15% 18%, rgba(100,104,176,0.12) 0%, rgba(100,104,176,0.00) 60%),
            radial-gradient(1100px 800px at 85% 82%, rgba(111,163,173,0.10) 0%, rgba(111,163,173,0.00) 65%),
            linear-gradient(135deg, #070a20 0%, #0b0f23 22%, #141a2e 45%, #1a2037 68%, #070a20 100%);
        color: #d5d9d5;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title (unchanged) */
    h1 {
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        text-align: center;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        background: none !important;
        text-shadow: none !important;
        margin-bottom: 0.5em;
    }

    /* Subheader (unchanged) */
    h3 {
        text-align: center;
        font-size: 1.6rem !important;
        margin-top: 2em;
        color: #cfd3cf;
        opacity: 0.9;
    }

    /* Style buttons as cards */
    .stButton > button {
        background: rgba(255,255,255,0.05);
        border-radius: 18px;
        padding: 1.5em;
        margin: 1em 0;
        text-align: center;
        transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(213,217,213,0.10);
        box-shadow: 0 10px 26px rgba(0,0,0,0.55);
        color: #d5d9d5;
        font-size: 1.2em;
        font-weight: 600;
        width: 100%;
        height: auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton > button:hover {
        transform: translateY(-6px);
        box-shadow:
            0 14px 34px rgba(0,0,0,0.62),
            0 0 20px rgba(100,104,176,0.28),
            0 0 14px rgba(111,163,173,0.20);
        border-color: rgba(111,163,173,0.35);
    }

    /* Tagline (unchanged) */
    .tagline {
        text-align: center;
        font-style: italic;
        margin-top: 3em;
        color: #555e70;
    }
    </style>
""", unsafe_allow_html=True)

# ====== HEADER ======
st.title("DSA Learning Hub — Learn by Playing")
st.caption("Who said DSA is hard? Make every step visible.")

# ====== INTRO ======
st.write(
    "Welcome to your interactive, game-like Data Structures & Algorithms playground. "
    "Input your own data, choose a module, and watch algorithms come alive step-by-step "
    "with controls like play, pause, step and Hands on Learning"
)

# ====== MODULES GRID ======
modules = [
    {"name": "Sorting", "page": "1_Sorting"},
    {"name": "Searching", "page": "2_Searching"},
    {"name": "Linked List", "page": "3_Linked_List"},
    {"name": "Stack & Queue", "page": "4_Stack_Queue"},
    {"name": "Trees", "page": "5_Trees"},
    {"name": "Graphs", "page": "6_Graphs"},
]

cols = st.columns(3)
for i, module in enumerate(modules):
    with cols[i % 3]:
        if st.button(module["name"], key=f"btn_{module['name']}"):
            st.switch_page(f"pages/{module['page']}.py")

# ====== TAGLINES ======
st.markdown("<div class='tagline'>DSA made fun: learn by playing, master by doing.</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Make every step visible. Make every concept click.</div>", unsafe_allow_html=True)
