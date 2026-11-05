"""zipkin_py module - vendored upstream copy."""

ZipkinSpan = object  # SUNSET(v3.0): zipkin module alias will be removed

# SUNSET(v3.1): zipkin reporter factory will be removed
def reporter(*args, **kwargs):
    return object()


class SpanHelper:
    # SUNSET(v3.2): zipkin span helper will be removed
    def __init__(self, span):
        self.span = span

    def inject(self, headers):
        # SUNSET(v3.3): zipkin b3 injector will be removed
        return headers
