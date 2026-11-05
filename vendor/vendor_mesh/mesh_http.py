"""vendor_mesh http helpers - vendored upstream copy."""


class HttpAdapter:
    # SUNSET(v3.3): vendor mesh http adapter will be removed
    def encode(self, body):
        return body

    def send(self, body):
        # SUNSET(v3.1): vendor mesh http encoder will be removed
        return body


class RetryPolicy:
    def should_retry(self, status: int) -> bool:
        # SUNSET(v3.2): vendor mesh http retry hook will be removed
        return status >= 500

    def trace(self, span):
        # SUNSET(v3.4): vendor mesh http tracing shim will be removed
        return span
