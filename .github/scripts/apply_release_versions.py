#!/usr/bin/env python3
"""Apply core/app release versions to the files consumed by platform builds."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def fail(message: str) -> None:
    print(f"release version setup: {message}", file=sys.stderr)
    raise SystemExit(1)


def replace(path: str, pattern: str, replacement: str, *, minimum: int = 1) -> None:
    file_path = ROOT / path
    with file_path.open(newline="") as source:
        contents = source.read()
    updated, count = re.subn(pattern, replacement, contents, flags=re.MULTILINE)
    if count < minimum:
        fail(f"expected at least {minimum} version field(s) in {path}, found {count}")
    with file_path.open("w", newline="") as destination:
        destination.write(updated)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: apply_release_versions.py CORE_VERSION APP_VERSION")

    core_version, app_version = (version.removeprefix("v") for version in sys.argv[1:])
    core_match = VERSION.fullmatch(core_version)
    app_match = VERSION.fullmatch(app_version)
    if not core_match or not app_match:
        fail("versions must be semantic versions in MAJOR.MINOR.PATCH form")

    major, minor, patch = (int(part) for part in app_match.groups())
    if max(major, minor, patch) > 99:
        fail("app version components must not exceed 99 to fit the build number")
    build_number = major * 10000 + minor * 100 + patch

    replace(
        r"dependencies.properties",
        r"^core\.version=[^\r\n]*(?=\r?$)",
        f"core.version={core_version}",
    )
    replace(r"pubspec.yaml", r"^version:[^\r\n]*(?=\r?$)", f"version: {app_version}+{build_number}")
    replace(
        r"windows/packaging/msix/make_config.yaml",
        r"^msix_version:[^\r\n]*(?=\r?$)",
        f"msix_version: {app_version}.0",
    )
    replace(
        r"ios/Runner.xcodeproj/project.pbxproj",
        r"^([ \t]*CURRENT_PROJECT_VERSION[ \t]*=[ \t]*)\d+(;)(?=\r?$)",
        rf"\g<1>{build_number}\2",
    )
    replace(
        r"ios/Runner.xcodeproj/project.pbxproj",
        r"^([ \t]*MARKETING_VERSION[ \t]*=[ \t]*)[^;\r\n]+(;)(?=\r?$)",
        rf"\g<1>{app_version}\2",
    )
    print(f"Using hiddify-core {core_version}, app {app_version} ({build_number})")


if __name__ == "__main__":
    main()