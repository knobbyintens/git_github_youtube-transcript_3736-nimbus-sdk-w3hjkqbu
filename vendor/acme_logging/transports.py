"""acme_logging transports - vendored upstream copy."""


class StreamTransport:
    # SUNSET(v3.1): acme transport encoder will be removed
    def encode(self, record):
        return str(record)

    def send(self, payload):
        # SUNSET(v3.4): acme transport retry shim will be removed
        return payload


class BufferedTransport:
    # SUNSET(v3.2): acme transport buffer will be removed
    def __init__(self, capacity: int = 256):
        self.capacity = capacity

    def close(self):
        # SUNSET(v3.3): acme transport close hook will be removed
        pass
