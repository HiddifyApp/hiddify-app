#!/usr/bin/env python3
"""Write <out-dir>/hiddify-ios-source.json: an AltStore-format app source for the iOS IPA, so
users add one URL in Feather, ESign, SideStore, AltStore or Scarlet and get every update there.
The release attaches it, so .../releases/latest/download/hiddify-ios-source.json always points
at the newest version.

Usage: make_ios_source.py <out-dir> <version> [repo]
"""

import datetime
import json
import os
import sys
from pathlib import Path

IPA = "Hiddify-iOS-Jailbreak.ipa"


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    out, version = Path(sys.argv[1]), sys.argv[2].removeprefix("v")
    repo = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("GITHUB_REPOSITORY", "HiddifyApp/hiddify-app")
    ipa = out / IPA
    if not ipa.is_file():
        print(f"{ipa} not found; no iOS source written")
        return 0

    raw = f"https://raw.githubusercontent.com/{repo}/main"
    icon = f"{raw}/android/app/src/main/ic_launcher-playstore.png"
    description = (
        "Fast, secure access to the open internet. Supports Sing-box, V2ray, Reality, Hysteria, "
        "TUIC, WireGuard and more.\n\nThe VPN works only when the certificate you sign with "
        "allows Network Extensions (packet tunnel)."
    )
    source = {
        "name": "Hiddify",
        "identifier": f"io.github.{repo.split('/')[0].lower()}.hiddify",
        "subtitle": "Hiddify for iPhone",
        "description": description,
        "iconURL": icon,
        "website": "https://hiddify.org",
        "tintColor": "#5A5AE6",
        "apps": [
            {
                "name": "Hiddify",
                "bundleIdentifier": "apple.hiddify.com",
                "developerName": "Hiddify",
                "subtitle": "Fast, secure access to the open internet",
                "localizedDescription": description,
                "iconURL": icon,
                "tintColor": "#5A5AE6",
                "category": "utilities",
                "versions": [
                    {
                        "version": version,
                        "date": datetime.date.today().isoformat(),
                        "localizedDescription": f"https://github.com/{repo}/releases/tag/v{version}",
                        "downloadURL": f"https://github.com/{repo}/releases/download/v{version}/{IPA}",
                        "size": ipa.stat().st_size,
                        "minOSVersion": "15.5",
                    }
                ],
                "appPermissions": {
                    "entitlements": [
                        "com.apple.developer.networking.networkextension",
                        "com.apple.developer.networking.vpn.api",
                        "com.apple.security.application-groups",
                    ],
                    "privacy": {},
                },
            }
        ],
        "news": [],
    }
    (out / "hiddify-ios-source.json").write_text(json.dumps(source, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote iOS source for {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
