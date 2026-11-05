# Nimbus SDK Deprecation Registry

This registry is maintained by hand by the SDK release owners. It lists the
public deprecations that have been approved for publication. It is deliberately
a curated subset of the markers found in the source tree: internal helpers,
vendored third-party copies, experimental modules, tests, examples and release
tooling are out of scope.

Entry format:

    - <path>:<line> | <target-release> | <description>

## Blocking removals (v3.0)

- src/nimbus/client.py:30 | v3.0 | Remove synchronous flush alias send_flush
- src/nimbus/config.py:25 | v3.0 | Reject log_level=DEBUG_VERBOSE spelling
- src/nimbus/exporters/otlp.py:14 | v3.0 | Remove insecure default endpoint http://localhost:4317
- src/nimbus/sampling.py:23 | v3.0 | Drop ratio sampler float shorthand
- src/nimbus/security/auth.py:20 | v3.0 | Remove api_key query-string authentication

## Planned removals

- src/nimbus/client.py:17 | v3.2 | Remove legacy timeout=seconds constructor argument
- src/nimbus/client.py:36 | v3.1 | Drop client.send_batch in favour of the batch context manager
- src/nimbus/config.py:22 | v3.1 | Drop NIMBUS_LEGACY_ENDPOINT environment variable
- src/nimbus/config.py:36 | v3.2 | Remove YAML config loader nimbus.load_yaml_config
- src/nimbus/context.py:18 | v3.2 | Remove attach_context(key, value) single-pair form
- src/nimbus/exporters/otlp.py:26 | v3.2 | Drop TLS exporter legacy cert flag
- src/nimbus/exporters/prometheus.py:13 | v3.1 | Remove process metrics auto-registration
- src/nimbus/exporters/prometheus.py:21 | v3.4 | Drop deprecated namespace argument fallback
- src/nimbus/integrations/django.py:15 | v3.2 | Drop NIMBUS_DJANGO_TRACE_HEADERS setting
- src/nimbus/integrations/flask.py:12 | v3.3 | Remove Flask extension init_app auto-config
- src/nimbus/metrics.py:14 | v3.1 | Drop Counter.cap attribute from the public API
- src/nimbus/metrics.py:26 | v3.3 | Remove legacy percentile(50) positional shorthand
- src/nimbus/sampling.py:17 | v3.1 | Remove ParentBasedSampler alias
- src/nimbus/security/auth.py:14 | v3.2 | Drop bearer_token positional constructor argument
- src/nimbus/security/redaction.py:12 | v3.1 | Remove redact_all default fallback
