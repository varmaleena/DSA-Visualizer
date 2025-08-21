from typing import Generator, List, Any, Optional
from core.models.frame import Frame


def _f(step, values, desc, hl=None, vars=None, stats=None):
    return Frame(
        step=step,
        view=values[:],
        narration=desc,
        highlights=hl or {},
        data=vars or {},
        metrics=stats or {},
    )


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None  # For singly and circular
        self.prev = None  # For doubly


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Optional for efficiency

    def to_list(self) -> List[Any]:
        """Convert linked list to Python list for visualization."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # Insert at head
    def insert_head_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0

        current_list = self.to_list()

        # Start
        yield _f(
            step, current_list, "Start: insert at head (singly linked)",
            hl={"head": 0 if current_list else None},
            vars={"new_value": x, "old_head": 0 if current_list else None},
            stats={"insertions": inserts}
        ); step += 1

        # New head and link
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"New head {x} points to old head",
            hl={"head": 0},
            vars={"new_head": 0, "next_of_head": 1 if len(new_list) > 1 else None},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Insert at tail
    def insert_tail_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0
        current_list = self.to_list()
        tail_idx = len(current_list) - 1 if current_list else None

        yield _f(
            step, current_list, "Start: insert at tail (singly linked)",
            hl={"tail": tail_idx},
            vars={"new_value": x, "tail": tail_idx},
            stats={"insertions": inserts}
        ); step += 1

        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"Append {x} at tail",
            hl={"tail": len(new_list) - 1},
            vars={"old_tail": tail_idx, "new_tail": len(new_list) - 1},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Search first occurrence
    def search_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        current_list = self.to_list()

        yield _f(
            step, current_list, f"Start: search for {x} (singly linked)",
            hl={"head": 0 if current_list else None},
            vars={"target": x, "i": None, "val": None},
            stats={"comparisons": comps}
        ); step += 1

        current = self.head
        i = 0
        while current:
            comps += 1
            yield _f(
                step, current_list, f"Check node {i}",
                hl={"current": i},
                vars={"target": x, "i": i, "val": current.value},
                stats={"comparisons": comps}
            ); step += 1

            if current.value == x:
                yield _f(
                    step, current_list, f"Found {x} at index {i}",
                    hl={"found": i},
                    vars={"target": x, "i": i},
                    stats={"comparisons": comps}
                ); step += 1
                return
            current = current.next
            i += 1

        yield _f(
            step, current_list, f"{x} not found",
            vars={"target": x},
            stats={"comparisons": comps}
        ); step += 1

    # Delete first occurrence by value
    def delete_value_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        deletes = 0
        links_changed = 0
        current_list = self.to_list()

        if not current_list:
            yield _f(
                step, current_list, "List empty; nothing to delete (singly linked)",
                vars={"target": x},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        yield _f(
            step, current_list, f"Start: delete value {x} (singly linked)",
            hl={"head": 0, "tail": len(current_list) - 1},
            vars={"target": x, "prev": None, "curr": 0},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1

        # Compare head
        comps += 1
        if self.head.value == x:
            deletes += 1
            links_changed += 1
            self.head = self.head.next
            if not self.head:
                self.tail = None
            new_list = self.to_list()
            yield _f(
                step, current_list, f"Compare head with {x}",
                hl={"current": 0, "head": 0},
                vars={"target": x, "prev": None, "curr": 0, "val": current_list[0]},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, f"Delete head {x}",
                hl={"head": 0 if new_list else None},
                vars={"new_head": 0 if new_list else None},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, "Done.",
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        # Traverse with prev/curr
        prev = self.head
        current = self.head.next
        i = 1
        while current:
            comps += 1
            yield _f(
                step, current_list, "Traverse: move prev/curr forward",
                hl={"prev": i-1, "current": i},
                vars={"target": x, "prev": i-1, "curr": i, "val": current.value},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1

            if current.value == x:
                deletes += 1
                links_changed += 1
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                new_list = self.to_list()
                yield _f(
                    step, current_list, f"Found {x} at {i}; unlink it",
                    hl={"prev": i-1, "current": i},
                    vars={"target": x, "prev": i-1, "curr": i},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Node removed; prev.next skips current",
                    hl={"prev": i-1 if i-1 < len(new_list) else None, "tail": len(new_list) - 1 if new_list else None},
                    vars={"new_length": len(new_list)},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Done.",
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                return

            prev = current
            current = current.next
            i += 1

        yield _f(
            step, current_list, f"{x} not found; no deletion",
            vars={"target": x},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self) -> List[Any]:
        """Convert doubly linked list to Python list for visualization."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # Insert at head
    def insert_head_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0

        current_list = self.to_list()

        # Start
        yield _f(
            step, current_list, "Start: insert at head (doubly linked)",
            hl={"head": 0 if current_list else None},
            vars={"new_value": x, "old_head": 0 if current_list else None},
            stats={"insertions": inserts}
        ); step += 1

        new_node = Node(x)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"New head {x} points to old head; old head.prev to new",
            hl={"head": 0},
            vars={"new_head": 0, "next_of_head": 1 if len(new_list) > 1 else None},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Insert at tail
    def insert_tail_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0
        current_list = self.to_list()
        tail_idx = len(current_list) - 1 if current_list else None

        yield _f(
            step, current_list, "Start: insert at tail (doubly linked)",
            hl={"tail": tail_idx},
            vars={"new_value": x, "tail": tail_idx},
            stats={"insertions": inserts}
        ); step += 1

        new_node = Node(x)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"Append {x} at tail; new.prev to old tail; old.next to new",
            hl={"tail": len(new_list) - 1},
            vars={"old_tail": tail_idx, "new_tail": len(new_list) - 1},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Search first occurrence
    def search_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        current_list = self.to_list()

        yield _f(
            step, current_list, f"Start: search for {x} (doubly linked)",
            hl={"head": 0 if current_list else None},
            vars={"target": x, "i": None, "val": None},
            stats={"comparisons": comps}
        ); step += 1

        current = self.head
        i = 0
        while current:
            comps += 1
            yield _f(
                step, current_list, f"Check node {i}",
                hl={"current": i},
                vars={"target": x, "i": i, "val": current.value},
                stats={"comparisons": comps}
            ); step += 1

            if current.value == x:
                yield _f(
                    step, current_list, f"Found {x} at index {i}",
                    hl={"found": i},
                    vars={"target": x, "i": i},
                    stats={"comparisons": comps}
                ); step += 1
                return
            current = current.next
            i += 1

        yield _f(
            step, current_list, f"{x} not found",
            vars={"target": x},
            stats={"comparisons": comps}
        ); step += 1

    # Delete first occurrence by value
    def delete_value_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        deletes = 0
        links_changed = 0
        current_list = self.to_list()

        if not current_list:
            yield _f(
                step, current_list, "List empty; nothing to delete (doubly linked)",
                vars={"target": x},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        yield _f(
            step, current_list, f"Start: delete value {x} (doubly linked)",
            hl={"head": 0, "tail": len(current_list) - 1},
            vars={"target": x, "prev": None, "curr": 0},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1

        # Compare head
        comps += 1
        if self.head.value == x:
            deletes += 1
            links_changed += 1
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            new_list = self.to_list()
            yield _f(
                step, current_list, f"Compare head with {x}",
                hl={"current": 0, "head": 0},
                vars={"target": x, "prev": None, "curr": 0, "val": current_list[0]},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, f"Delete head {x}; update new head.prev to None",
                hl={"head": 0 if new_list else None},
                vars={"new_head": 0 if new_list else None},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, "Done.",
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        # Traverse with curr
        current = self.head
        i = 0
        while current:
            comps += 1
            yield _f(
                step, current_list, "Traverse: check current",
                hl={"current": i},
                vars={"target": x, "curr": i, "val": current.value},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1

            if current.value == x:
                deletes += 1
                links_changed += 2  # Update prev.next and next.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                new_list = self.to_list()
                yield _f(
                    step, current_list, f"Found {x} at {i}; unlink it (update prev.next and next.prev)",
                    hl={"current": i},
                    vars={"target": x, "curr": i},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Node removed; links updated",
                    hl={"tail": len(new_list) - 1 if new_list else None},
                    vars={"new_length": len(new_list)},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Done.",
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                return

            current = current.next
            i += 1

        yield _f(
            step, current_list, f"{x} not found; no deletion",
            vars={"target": x},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self) -> List[Any]:
        """Convert circular linked list to Python list for visualization (breaks at head)."""
        if not self.head:
            return []
        result = []
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result

    # Insert at head
    def insert_head_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0

        current_list = self.to_list()

        # Start
        yield _f(
            step, current_list, "Start: insert at head (circular linked)",
            hl={"head": 0 if current_list else None, "circular": len(current_list) - 1 if current_list else None},
            vars={"new_value": x, "old_head": 0 if current_list else None},
            stats={"insertions": inserts}
        ); step += 1

        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Circular
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"New head {x} points to old head; tail points to new head",
            hl={"head": 0, "circular": len(new_list) - 1},
            vars={"new_head": 0, "next_of_head": 1 if len(new_list) > 1 else None},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Insert at tail
    def insert_tail_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        inserts = 0
        current_list = self.to_list()
        tail_idx = len(current_list) - 1 if current_list else None

        yield _f(
            step, current_list, "Start: insert at tail (circular linked)",
            hl={"tail": tail_idx, "circular": tail_idx if current_list else None},
            vars={"new_value": x, "tail": tail_idx},
            stats={"insertions": inserts}
        ); step += 1

        new_node = Node(x)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head  # New tail points to head
            self.tail.next = new_node
            self.tail = new_node
        inserts += 1
        new_list = self.to_list()
        yield _f(
            step, new_list, f"Append {x} at tail; new tail points to head",
            hl={"tail": len(new_list) - 1, "circular": len(new_list) - 1},
            vars={"old_tail": tail_idx, "new_tail": len(new_list) - 1},
            stats={"insertions": inserts}
        ); step += 1

        yield _f(step, new_list, "Done.", stats={"insertions": inserts}); step += 1

    # Search first occurrence
    def search_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        current_list = self.to_list()

        yield _f(
            step, current_list, f"Start: search for {x} (circular linked)",
            hl={"head": 0 if current_list else None},
            vars={"target": x, "i": None, "val": None},
            stats={"comparisons": comps}
        ); step += 1

        if not self.head:
            yield _f(
                step, current_list, f"{x} not found (empty list)",
                vars={"target": x},
                stats={"comparisons": comps}
            ); step += 1
            return

        current = self.head
        i = 0
        while True:
            comps += 1
            yield _f(
                step, current_list, f"Check node {i}",
                hl={"current": i},
                vars={"target": x, "i": i, "val": current.value},
                stats={"comparisons": comps}
            ); step += 1

            if current.value == x:
                yield _f(
                    step, current_list, f"Found {x} at index {i}",
                    hl={"found": i},
                    vars={"target": x, "i": i},
                    stats={"comparisons": comps}
                ); step += 1
                return
            current = current.next
            i += 1
            if current == self.head:
                break

        yield _f(
            step, current_list, f"{x} not found",
            vars={"target": x},
            stats={"comparisons": comps}
        ); step += 1

    # Delete first occurrence by value
    def delete_value_frames(self, x: Any) -> Generator[Frame, None, None]:
        step = 0
        comps = 0
        deletes = 0
        links_changed = 0
        current_list = self.to_list()

        if not current_list:
            yield _f(
                step, current_list, "List empty; nothing to delete (circular linked)",
                vars={"target": x},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        yield _f(
            step, current_list, f"Start: delete value {x} (circular linked)",
            hl={"head": 0, "tail": len(current_list) - 1},
            vars={"target": x, "prev": None, "curr": 0},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1

        # Compare head
        comps += 1
        if self.head.value == x:
            deletes += 1
            links_changed += 1
            if self.head == self.tail:  # Single node
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            new_list = self.to_list()
            yield _f(
                step, current_list, f"Compare head with {x}",
                hl={"current": 0, "head": 0},
                vars={"target": x, "prev": None, "curr": 0, "val": current_list[0]},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, f"Delete head {x}; tail points to new head",
                hl={"head": 0 if new_list else None},
                vars={"new_head": 0 if new_list else None},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            yield _f(
                step, new_list, "Done.",
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1
            return

        # Traverse
        current = self.head.next
        prev = self.head
        i = 1
        while current != self.head:
            comps += 1
            yield _f(
                step, current_list, "Traverse: check current",
                hl={"prev": i-1, "current": i},
                vars={"target": x, "prev": i-1, "curr": i, "val": current.value},
                stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
            ); step += 1

            if current.value == x:
                deletes += 1
                links_changed += 1
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                new_list = self.to_list()
                yield _f(
                    step, current_list, f"Found {x} at {i}; unlink it (prev.next to current.next)",
                    hl={"prev": i-1, "current": i},
                    vars={"target": x, "prev": i-1, "curr": i},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Node removed; links updated",
                    hl={"tail": len(new_list) - 1 if new_list else None},
                    vars={"new_length": len(new_list)},
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                yield _f(
                    step, new_list, "Done.",
                    stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
                ); step += 1
                return

            prev = current
            current = current.next
            i += 1

        yield _f(
            step, current_list, f"{x} not found; no deletion",
            vars={"target": x},
            stats={"comparisons": comps, "deletions": deletes, "links_changed": links_changed}
        ); step += 1


# Test (optional)
if __name__ == "__main__":
    sll = SinglyLinkedList()
    for frame in sll.insert_head_frames(10):
        print(frame.to_dict())

    dll = DoublyLinkedList()
    for frame in dll.insert_tail_frames(20):
        print(frame.to_dict())

    cll = CircularLinkedList()
    for frame in cll.search_frames(10):
        print(frame.to_dict())
