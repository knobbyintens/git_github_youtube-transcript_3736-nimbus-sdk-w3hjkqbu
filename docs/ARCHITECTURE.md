# Architecture notes

The SDK is organised into four layers:

1. `client` - buffering and delivery entry points;
2. `exporters` - transport implementations (OTLP, Prometheus);
3. `security` - authentication and redaction helpers;
4. `integrations` - framework specific wiring.

Experimental code lives under `src/nimbus/experimental` and is not part of
the published package surface.
