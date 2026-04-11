#!/usr/bin/env python3
"""Read config/test-rfes.yaml and print RFE IDs, one per line.

Usage:
    python3 scripts/list-rfe-ids.py                  # all IDs
    python3 scripts/list-rfe-ids.py --baseline        # only baseline RFEs
    python3 scripts/list-rfe-ids.py --no-baseline     # exclude baseline RFEs
"""

import argparse
import sys
from pathlib import Path

import yaml


def main():
    parser = argparse.ArgumentParser(description="List RFE IDs from config")
    parser.add_argument(
        "--config",
        default=Path(__file__).resolve().parent.parent / "config" / "test-rfes.yaml",
        help="Path to test-rfes.yaml",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--baseline", action="store_true", help="Only baseline RFEs")
    group.add_argument("--no-baseline", action="store_true", help="Exclude baseline RFEs")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Error: {config_path} not found", file=sys.stderr)
        sys.exit(1)

    with open(config_path) as f:
        data = yaml.safe_load(f)

    for rfe in data.get("test_rfes", []):
        is_baseline = rfe.get("baseline", False)
        if args.baseline and not is_baseline:
            continue
        if args.no_baseline and is_baseline:
            continue
        print(rfe["id"])


if __name__ == "__main__":
    main()
