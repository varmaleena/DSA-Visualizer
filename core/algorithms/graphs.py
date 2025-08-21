from typing import Generator, Dict, Any, List, Tuple
from collections import deque, defaultdict
import heapq
from core.models.frame import Frame

# Helper to build highlights dict (from your searching.py)
def HL(**kwargs) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # {node: [(neighbor, weight)]}

    def add_edge(self, u, v, weight=1, directed=False):
        self.graph[u].append((v, weight))
        if not directed:
            self.graph[v].append((u, weight))

    def get_nodes(self):
        return list(self.graph.keys())

    def bfs_frames(self, start) -> Generator[Frame, None, None]:
        visited = set()
        queue = deque([start])
        step = 0
        visited.add(start)

        yield Frame(
            step=step,
            view=self.graph,
            narration=f"Start BFS from node {start}.",
            data={"queue": list(queue)},
            metrics={"visited": len(visited)},
            highlights={start: "yellow"},  # Current
        )
        step += 1

        while queue:
            current = queue.popleft()
            yield Frame(
                step=step,
                view=self.graph,
                narration=f"Visit node {current}.",
                data={"queue": list(queue), "current": current},
                metrics={"visited": len(visited)},
                highlights={current: "green"},  # Visited
            )
            step += 1

            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    yield Frame(
                        step=step,
                        view=self.graph,
                        narration=f"Enqueue neighbor {neighbor}.",
                        data={"queue": list(queue)},
                        metrics={"visited": len(visited)},
                        highlights={neighbor: "yellow"},
                    )
                    step += 1

        yield Frame(
            step=step,
            view=self.graph,
            narration="BFS complete.",
            data={},
            metrics={"visited": len(visited)},
            highlights={},
        )

    def dfs_frames(self, start) -> Generator[Frame, None, None]:
        visited = set()
        stack = [start]
        step = 0

        yield Frame(
            step=step,
            view=self.graph,
            narration=f"Start DFS from node {start}.",
            data={"stack": stack},
            metrics={"visited": 0},
            highlights={start: "yellow"},
        )
        step += 1

        while stack:
            current = stack[-1]
            if current not in visited:
                visited.add(current)
                yield Frame(
                    step=step,
                    view=self.graph,
                    narration=f"Visit node {current}.",
                    data={"stack": stack, "current": current},
                    metrics={"visited": len(visited)},
                    highlights={current: "green"},
                )
                step += 1

            popped = False
            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    yield Frame(
                        step=step,
                        view=self.graph,
                        narration=f"Push neighbor {neighbor}.",
                        data={"stack": stack},
                        metrics={"visited": len(visited)},
                        highlights={neighbor: "yellow"},
                    )
                    step += 1
                    popped = True
                    break

            if not popped:
                stack.pop()

        yield Frame(
            step=step,
            view=self.graph,
            narration="DFS complete.",
            data={},
            metrics={"visited": len(visited)},
            highlights={},
        )

    def dijkstra_frames(self, start) -> Generator[Frame, None, None]:
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)
        step = 0

        yield Frame(
            step=step,
            view=self.graph,
            narration=f"Start Dijkstra from node {start}.",
            data={"distances": distances},
            metrics={"updated": 0},
            highlights={start: "yellow"},
        )
        step += 1

        while pq:
            dist, current = heapq.heappop(pq)
            if dist > distances[current]:
                continue

            yield Frame(
                step=step,
                view=self.graph,
                narration=f"Process node {current} with dist {dist}.",
                data={"current": current, "dist": dist},
                metrics={"updated": len(distances)},
                highlights={current: "green"},
            )
            step += 1

            for neighbor, weight in self.graph[current]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
                    yield Frame(
                        step=step,
                        view=self.graph,
                        narration=f"Update dist to {neighbor} as {new_dist}.",
                        data={"updated": neighbor, "new_dist": new_dist},
                        metrics={"updated": len(distances)},
                        highlights={neighbor: "yellow"},
                    )
                    step += 1

        yield Frame(
            step=step,
            view=self.graph,
            narration="Dijkstra complete.",
            data={"final_distances": distances},
            metrics={},
            highlights={},
        )

# Test (optional)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    for frame in g.bfs_frames(0):
        print(frame.to_dict())
