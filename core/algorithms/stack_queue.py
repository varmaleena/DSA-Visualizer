from typing import Generator, List, Any, Dict
from core.models.frame import Frame

def _f(step, values, desc, hl=None, vars=None):
    return Frame(step=step, view=values[:], narration=desc, highlights=hl or {}, data=vars or {})

# -----------------------------
# Stack (LIFO)
# -----------------------------
def stack_push_frames(values: List[Any], x: Any) -> Generator[Frame, None, None]:
    a = values[:]
    step = 0

    yield _f(step, a, "Start push()", hl={"top": len(a)-1 if a else None}, vars={"push_value": x}); step += 1
    a.append(x)
    yield _f(step, a, f"Push {x} to top", hl={"top": len(a)-1, "current": len(a)-1}, vars={"top": len(a)-1}); step += 1
    yield _f(step, a, "Done."); step += 1

def stack_pop_frames(values: List[Any]) -> Generator[Frame, None, Any]:
    a = values[:]
    step = 0

    if not a:
        yield _f(step, a, "Pop requested, but stack is empty."); step += 1
        return

    yield _f(step, a, "Start pop()", hl={"top": len(a)-1}, vars={"top": len(a)-1}); step += 1
    top_val = a[-1]
    yield _f(step, a, f"Peek top = {top_val}", hl={"top": len(a)-1, "current": len(a)-1}, vars={"top": len(a)-1, "value": top_val}); step += 1
    a.pop()
    yield _f(step, a, f"Remove top {top_val}", hl={"moved": len(a)}, vars={"popped": top_val}); step += 1
    yield _f(step, a, "Done."); step += 1

# -----------------------------
# Queue (FIFO)
# -----------------------------
def queue_enqueue_frames(values: List[Any], x: Any) -> Generator[Frame, None, None]:
    q = values[:]
    step = 0
    front = 0 if q else None
    rear = len(q)-1 if q else None

    yield _f(step, q, "Start enqueue()", hl={"front": front, "rear": rear}, vars={"enqueue_value": x}); step += 1
    q.append(x)
    yield _f(step, q, f"Insert {x} at rear", hl={"front": 0 if q else None, "rear": len(q)-1, "current": len(q)-1}, vars={"rear": len(q)-1}); step += 1
    yield _f(step, q, "Done."); step += 1

def queue_dequeue_frames(values: List[Any]) -> Generator[Frame, None, Any]:
    q = values[:]
    step = 0
    if not q:
        yield _f(step, q, "Dequeue requested, but queue is empty."); step += 1
        return

    yield _f(step, q, "Start dequeue()", hl={"front": 0, "rear": len(q)-1}, vars={"front": 0, "rear": len(q)-1}); step += 1
    front_val = q[0]
    yield _f(step, q, f"Peek front = {front_val}", hl={"front": 0, "current": 0}, vars={"front": 0, "value": front_val}); step += 1
    q.pop(0)
    yield _f(step, q, f"Remove front {front_val}", hl={"moved": 0, "front": 0 if q else None, "rear": len(q)-1 if q else None}, vars={"dequeued": front_val}); step += 1
    yield _f(step, q, "Done."); step += 1
