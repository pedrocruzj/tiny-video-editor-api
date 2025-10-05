class DotDict:
    def __init__(self, data):
        self.data = data

    def get(self, path, default=None):
        keys = path.split(".")
        current = self.data
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key, default)
            else:
                return default
        return current
