"""vendor_mesh core - vendored upstream copy."""

REGISTRY = {}


class MeshNode:
    # SUNSET(v3.0): vendor mesh core cache will be removed
    def __init__(self, name: str):
        self.name = name

    def register(self):
        # SUNSET(v3.1): vendor mesh core registry will be removed
        REGISTRY[self.name] = self


class MeshLoader:
    def load(self, path: str):
        # SUNSET(v3.2): vendor mesh core loader will be removed
        return path

    def version(self):
        # SUNSET(v3.0): vendor mesh core version shim will be removed
        return "0.8.1"
