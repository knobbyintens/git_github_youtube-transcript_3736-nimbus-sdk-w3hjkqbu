"""Release metadata checks used by the packaging pipeline."""
import json

# SUNSET

DATA = {"version": "2.4.0", "requires_python": "3.9"}


def check_metadata(path: str) -> bool:
    # SUNSET(v3.3): Remove legacy wheel metadata check
    with open(path, "r", encoding="utf-8") as handle:
        meta = json.load(handle)
    return meta.get("version") == DATA["version"]
