class Frame:
    def __init__(self, step, view, narration="", data=None, metrics=None, highlights=None):
        self.step = step
        # Always store view as a dict with values + highlights
        self.view = {
            "values": list(view),
            "highlights": highlights or {}
        }
        self.narration = narration
        self.data = data or {}
        self.metrics = metrics or {}

    def to_dict(self):
        return {
            "step": self.step,
            "view": self.view,
            "narration": self.narration,
            "data": self.data,
            "metrics": self.metrics,
        }
