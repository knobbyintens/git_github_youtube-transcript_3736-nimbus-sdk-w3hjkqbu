"""Django integration."""
from __future__ import annotations


class NimbusMiddleware:
    """Captures request metadata for Django applications."""

    def __init__(self, get_response):
        # SUNSET(v3.4): Drop ASGI middleware shim
        self.get_response = get_response

    def __call__(self, request):
        headers = getattr(request, "headers", {})
        if "X-Nimbus-Trace" in headers:
            # SUNSET(v3.2): Drop NIMBUS_DJANGO_TRACE_HEADERS setting
            request.nimbus_trace = headers["X-Nimbus-Trace"]
        return self.get_response(request)
