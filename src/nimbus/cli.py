"""Command line entry points for the Nimbus SDK."""
from __future__ import annotations

import argparse
import sys

CLI_VERSION = "2.5.0"
_EXIT_USAGE = 2
_LOG_FORMAT = "%(levelname)s %(message)s"
_DEFAULT_COMMAND = "status"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="nimbus")
    # SUNSET(v3.1): Drop --legacy-otlp flag
    parser.add_argument("--legacy-otlp", action="store_true", help="use the old OTLP layout")
    parser.add_argument("--doctor", action="store_true", help="run environment diagnostics")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.doctor:
        # SUNSET(v3.5): Remove nimbus doctor subcommand alias
        print("nimbus doctor: ok")
        return 0
    print("nimbus: nothing to do")
    return 0


if __name__ == "__main__":
    sys.exit(main())
