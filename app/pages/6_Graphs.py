import os
import sys
import time
import streamlit as st


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from core.algorithms.graphs import Graph
from core.views.graph_view import render_graph


st.set_page_config(page_title="Graph ", layout="wide")


# Data for all graph algorithms (GFG-style info)
graph_algorithms = {
    "BFS": {
        "description": """
- **Breadth-First Search (BFS)**: Explores graph level-by-level from a source node using a queue. Visits all neighbors before going deeper.
- **Use Cases**: Shortest path in unweighted graphs, connected components, social networks.
        """,
        "complexity": """
- **Time Complexity**: O(V + E) where V is vertices, E is edges.  
- **Space Complexity**: O(V).  
- **Graph Type**: Directed/Undirected.
        """,
        "code": {
            "Python": """
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as adjacency list
graph = {0: [1, 2], 1: [3], 2: [], 3: []}
bfs(graph, 0)  # Output: 0 1 2 3
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Number of Islands", "url": "https://leetcode.com/problems/number-of-islands/"},
            {"title": "Word Ladder", "url": "https://leetcode.com/problems/word-ladder/"},
            {"title": "Rotting Oranges", "url": "https://leetcode.com/problems/rotting-oranges/"}
        ],
        "resources": [
            {"title": "GFG: BFS", "url": "https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"},
            {"title": "Visualgo: BFS", "url": "https://visualgo.net/en/graphds"}
        ]
    },
    "DFS": {
        "description": """
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking, using recursion or a stack.
- **Use Cases**: Cycle detection, topological sorting, maze solving.
        """,
        "complexity": """
- **Time Complexity**: O(V + E).  
- **Space Complexity**: O(V) (recursion stack).  
- **Graph Type**: Directed/Undirected.
        """,
        "code": {
            "Python": """
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph as adjacency list
graph = {0: [1, 2], 1: [3], 2: [], 3: []}
dfs(graph, 0)  # Possible output: 0 1 3 2
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Number of Provinces", "url": "https://leetcode.com/problems/number-of-provinces/"},
            {"title": "Course Schedule", "url": "https://leetcode.com/problems/course-schedule/"},
            {"title": "Keys and Rooms", "url": "https://leetcode.com/problems/keys-and-rooms/"}
        ],
        "resources": [
            {"title": "GFG: DFS", "url": "https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/"},
            {"title": "Visualgo: DFS", "url": "https://visualgo.net/en/graphds"}
        ]
    },
    "Dijkstra": {
        "description": """
- **Dijkstra's Algorithm**: Finds the shortest path from a source to all nodes in a weighted graph with non-negative weights.
- **Use Cases**: GPS navigation, network routing, resource allocation.
        """,
        "complexity": """
- **Time Complexity**: O((V + E) log V) with priority queue.  
- **Space Complexity**: O(V).  
- **Graph Type**: Weighted, Directed/Undirected (non-negative weights).
        """,
        "code": {
            "Python": """
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# Example graph as adjacency list with weights
graph = {0: [(1, 1), (2, 4)], 1: [(3, 2)], 2: [(3, 6)], 3: []}
print(dijkstra(graph, 0))  # {0: 0, 1: 1, 2: 4, 3: 3}
            """,
            "Java": """
// Refer to GFG for full Java implementation.
            """,
            "C++": """
// Refer to GFG for full C++ implementation.
            """
        },
        "problems": [
            {"title": "Network Delay Time", "url": "https://leetcode.com/problems/network-delay-time/"},
            {"title": "Cheapest Flights Within K Stops", "url": "https://leetcode.com/problems/cheapest-flights-within-k-stops/"},
            {"title": "Path With Minimum Effort", "url": "https://leetcode.com/problems/path-with-minimum-effort/"}
        ],
        "resources": [
            {"title": "GFG: Dijkstra's Algorithm", "url": "https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"}
            
        ]
    }
}

st.title("Graph City")
st.caption("Watch graph traversals and shortest paths unfold step-by-step.")


# ===== DYNAMIC INFO BAR (Updates based on selected algorithm) =====
selected_algo = st.selectbox("Algorithm", list(graph_algorithms.keys()), index=0)

with st.expander(f"ℹ️ {selected_algo}: Overview, Code, Complexity, and Top LeetCode Problems", expanded=False):
    algo_data = graph_algorithms[selected_algo]
    
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


# Session state
if "frames_g" not in st.session_state:
    st.session_state.frames_g = []
if "idx_g" not in st.session_state:
    st.session_state.idx_g = 0
if "playing_g" not in st.session_state:
    st.session_state.playing_g = False


# Inputs
edges_text = st.text_input("Edges (e.g., 0-1,0-2,1-3)", "0-1,0-2,1-3")
try:
    edges = [tuple(map(int, e.split('-'))) for e in edges_text.split(',') if e.strip()]
except ValueError:
    st.error("Enter edges as comma-separated pairs (e.g., 0-1,0-2).")
    st.stop()


start_node = st.number_input("Start Node", value=0, step=1)


speed = st.slider("Speed (steps/sec)", 1, 10, 5)


# Build graph
def build_graph(edges):
    g = Graph()
    for u, v in edges:
        g.add_edge(u, v)
    return g


# Controls
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("Generate"):
    graph = build_graph(edges)
    if selected_algo == "BFS":
        st.session_state.frames_g = list(graph.bfs_frames(start_node))
    elif selected_algo == "DFS":
        st.session_state.frames_g = list(graph.dfs_frames(start_node))
    elif selected_algo == "Dijkstra":
        st.session_state.frames_g = list(graph.dijkstra_frames(start_node))
    st.session_state.idx_g = 0
    st.session_state.playing_g = False


if c2.button("Play"):
    st.session_state.playing_g = True


if c3.button("Pause"):
    st.session_state.playing_g = False


if c4.button("Step"):
    if st.session_state.frames_g:
        st.session_state.idx_g = min(st.session_state.idx_g + 1, len(st.session_state.frames_g) - 1)


if c5.button("Restart"):
    st.session_state.idx_g = 0
    st.session_state.playing_g = False


# Display
left, right = st.columns([3, 2])


def render_current():
    if not st.session_state.frames_g:
        st.info("Enter edges/start node, choose an algorithm, then click Generate.")
        return
    frame = st.session_state.frames_g[st.session_state.idx_g]
    with left:
        # Fixed: Extract highlights from frame.view (not frame.highlights)
        highlights = frame.view.get("highlights", {})
        render_graph(frame.view, title=f"Graph View — Step {frame.step}", highlights=highlights)
    with right:
        st.subheader("Narration")
        st.write(frame.narration)
        st.subheader("Data / Vars")
        st.json(frame.data)
        st.subheader("Metrics")
        st.json(frame.metrics)
    
    st.caption(f"Frame {st.session_state.idx_g + 1} / {len(st.session_state.frames_g)}")


# Animation loop
if st.session_state.playing_g and st.session_state.frames_g:
    render_current()
    if st.session_state.idx_g < len(st.session_state.frames_g) - 1:
        st.session_state.idx_g += 1
        time.sleep(1.0 / max(1, speed))
        st.rerun()
    else:
        st.session_state.playing_g = False
        st.rerun()
else:
    render_current()


st.markdown("---")
st.caption("Tip: Enter edges as pairs, select algo, and watch the traversal.")
