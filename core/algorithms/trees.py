# core/algorithms/trees.py (updated with MinHeap and MaxHeap)

from typing import Generator, Dict, Any
from collections import deque
from core.models.frame import Frame  # Assume this is your Frame class


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # For AVL


# Helper to build highlights dict (from your searching.py)
def HL(**kwargs) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}


def generate_view(root):
    """Generate a level-order list of node values for visualization. Returns [] if root is None."""
    if not root:
        return []
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


class BST:
    def __init__(self):
        self.root = None

    def insert_frames(self, value) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        current = self.root
        parent = None

        # Initial frame
        yield Frame(
            step=step,
            view=generate_view(self.root),
            narration="Start BST insertion.",
            data={"value": value},
            metrics={"comparisons": comps},
            highlights={},
        )
        step += 1

        while current:
            comps += 1
            yield Frame(
                step=step,
                view=generate_view(self.root),
                narration=f"Compare with node {current.value}.",
                data={"current": current.value, "value": value},
                metrics={"comparisons": comps},
                highlights={current.value: "yellow"},  # Highlight current comparison
            )
            step += 1

            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node = Node(value)
        if parent is None:
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        yield Frame(
            step=step,
            view=generate_view(self.root),
            narration=f"Inserted {value}.",
            data={"inserted": value},
            metrics={"comparisons": comps},
            highlights={value: "green"},  # Highlight inserted node
        )

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result


class AVL(BST):
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert_frames(self, value) -> Generator[Frame, None, None]:
        # Similar to BST but with balancing steps
        # For brevity, use BST logic; expand for rotations with yields
        yield from super().insert_frames(value)


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert_frames(self, value) -> Generator[Frame, None, None]:
        step = 0
        self.heap.append(value)
        yield Frame(
            step=step,
            view=self.heap[:],
            narration=f"Append {value} to min-heap",
            data={"value": value},
            metrics={},
            highlights={"append": [len(self.heap) - 1]},
        )
        step += 1

        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            yield Frame(
                step=step,
                view=self.heap[:],
                narration=f"Compare {self.heap[i]} with parent {self.heap[parent]}",
                data={"i": i, "parent": parent},
                metrics={"comparisons": 1},
                highlights={"compare": [i, parent]},
            )
            step += 1

            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                yield Frame(
                    step=step,
                    view=self.heap[:],
                    narration=f"Swap {self.heap[i]} with {self.heap[parent]}",
                    data={"i": i, "parent": parent},
                    metrics={"swaps": 1},
                    highlights={"swap": [i, parent]},
                )
                step += 1
                i = parent
            else:
                break

        yield Frame(
            step=step,
            view=self.heap[:],
            narration=f"Inserted {value} into min-heap",
            data={"inserted": value},
            metrics={},
            highlights={"inserted": [0]},  # Highlight root
        )


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert_frames(self, value) -> Generator[Frame, None, None]:
        step = 0
        self.heap.append(value)
        yield Frame(
            step=step,
            view=self.heap[:],
            narration=f"Append {value} to max-heap",
            data={"value": value},
            metrics={},
            highlights={"append": [len(self.heap) - 1]},
        )
        step += 1

        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            yield Frame(
                step=step,
                view=self.heap[:],
                narration=f"Compare {self.heap[i]} with parent {self.heap[parent]}",
                data={"i": i, "parent": parent},
                metrics={"comparisons": 1},
                highlights={"compare": [i, parent]},
            )
            step += 1

            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                yield Frame(
                    step=step,
                    view=self.heap[:],
                    narration=f"Swap {self.heap[i]} with {self.heap[parent]}",
                    data={"i": i, "parent": parent},
                    metrics={"swaps": 1},
                    highlights={"swap": [i, parent]},
                )
                step += 1
                i = parent
            else:
                break

        yield Frame(
            step=step,
            view=self.heap[:],
            narration=f"Inserted {value} into max-heap",
            data={"inserted": value},
            metrics={},
            highlights={"inserted": [0]},  # Highlight root
        )


# Test (optional)
if __name__ == "__main__":
    bst = BST()
    for frame in bst.insert_frames(10):
        print(frame.to_dict())

    min_heap = MinHeap()
    for frame in min_heap.insert_frames(10):
        print(frame.to_dict())

    max_heap = MaxHeap()
    for frame in max_heap.insert_frames(10):
        print(frame.to_dict())
