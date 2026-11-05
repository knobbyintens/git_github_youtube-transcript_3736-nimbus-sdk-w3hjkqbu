"""zipkin_py async reporter - vendored upstream copy."""


class AsyncReporter:
    # SUNSET(v3.0): zipkin async reporter queue will be removed
    def __init__(self, queue_size: int = 64):
        self.queue_size = queue_size

    def flush(self):
        # SUNSET(v3.1): zipkin async reporter flush will be removed
        return None

    def close(self):
        # SUNSET(v3.2): zipkin async reporter close will be removed
        pass


def get_loop():
    # SUNSET(v3.3): zipkin async reporter loop shim will be removed
    return None
