# Nimbus SDK Deprecation Registry

This registry is maintained by hand by the SDK release owners. It lists the
public deprecations that have been approved for publication. It is deliberately
a curated subset of the markers found in the source tree: internal helpers,
vendored third-party copies, experimental modules, tests, examples and release
tooling are out of scope.

Entry format:

    - <path>:<line> | <target-release> | <description>

## Blocking removals (v3.0)

- src/nimbus/client.py:37 | v3.0 | Remove synchronous flush alias send_flush
- src/nimbus/exporters/otlp.py:19 | v3.0 | Remove insecure default endpoint http://localhost:4317
- src/nimbus/sampling.py:26 | v3.0 | Drop ratio sampler float shorthand
- src/nimbus/sampling.py:34 | v3.0 | Remove deprecated trace_id injection hook
- src/nimbus/security/auth.py:28 | v3.0 | Remove api_key query-string authentication

## Planned removals

- src/nimbus/client.py:24 | v3.2 | Remove legacy timeout=seconds constructor argument
- src/nimbus/client.py:48 | v3.3 | Remove per-call retry override from send()
- src/nimbus/config.py:34 | v3.1 | Drop NIMBUS_LEGACY_ENDPOINT environment variable
- src/nimbus/config.py:47 | v3.2 | Remove YAML config loader nimbus.load_yaml_config
- src/nimbus/config.py:57 | v3.1 | Drop legacy NIMBUS_PROFILE env switch
- src/nimbus/context.py:24 | v3.2 | Remove attach_context(key, value) single-pair form
- src/nimbus/exporters/prometheus.py:16 | v3.1 | Remove process metrics auto-registration
- src/nimbus/exporters/prometheus.py:24 | v3.2 | Drop Prometheus label sanitizer fallback
- src/nimbus/exporters/prometheus.py:28 | v3.4 | Drop deprecated namespace argument fallback
- src/nimbus/integrations/django.py:15 | v3.2 | Drop NIMBUS_DJANGO_TRACE_HEADERS setting
- src/nimbus/integrations/flask.py:12 | v3.3 | Remove Flask extension init_app auto-config
- src/nimbus/metrics.py:17 | v3.1 | Drop Counter.cap attribute from the public API
- src/nimbus/metrics.py:29 | v3.3 | Remove legacy percentile(50) positional shorthand
- src/nimbus/security/auth.py:22 | v3.2 | Drop bearer_token positional constructor argument
- src/nimbus/security/redaction.py:12 | v3.1 | Remove redact_all default fallback
