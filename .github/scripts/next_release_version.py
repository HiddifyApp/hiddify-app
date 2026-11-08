#!/usr/bin/env python3
"""Choose a monotonically increasing app version for a personal release."""

import re
import sys


VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse(value: str) -> tuple[int, int, int] | None:
    value = value.removeprefix("v")
    match = VERSION.fullmatch(value)
    return tuple(map(int, match.groups())) if match else None


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 4:
        fail("usage: next_release_version.py APP_VERSION CORE_VERSION LATEST_RELEASE_VERSION")

    app_version, core_version, latest_release = map(parse, sys.argv[1:])
    if app_version is None or core_version is None:
        fail("app and core versions must use MAJOR.MINOR.PATCH")

    candidates = [app_version, core_version]
    if latest_release is not None:
        candidates.append(latest_release)
    selected = max(candidates)

    if latest_release is not None and selected <= latest_release:
        major, minor, patch = latest_release
        if patch < 99:
            selected = (major, minor, patch + 1)
        elif minor < 99:
            selected = (major, minor + 1, 0)
        elif major < 99:
            selected = (major + 1, 0, 0)
        else:
            fail("app version cannot be incremented within the build-number range")

    if max(selected) > 99:
        fail("version components must not exceed 99 to fit the build number")
    print(".".join(map(str, selected)))


if __name__ == "__main__":
    main()