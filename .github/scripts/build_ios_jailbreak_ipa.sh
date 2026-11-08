#!/usr/bin/env bash
# Builds out/Hiddify-iOS-Jailbreak.ipa: the iOS app without an Apple signature, fake-signed with
# ldid and its VPN entitlements so it installs on jailbroken iPhones (AppSync) and with TrollStore.
# Usage: build_ios_jailbreak_ipa.sh [flutter build args...]
set -euo pipefail

flutter build ios --release --no-codesign "$@"

app=build/ios/iphoneos/Runner.app
[[ -d "$app" ]] || { echo "::error::$app was not built" >&2; exit 1; }

command -v ldid >/dev/null || brew install ldid

work="$(mktemp -d)"
bundle_id="$(sed -n 's/^BASE_BUNDLE_IDENTIFIER=//p' ios/Base.xcconfig | head -n 1)"
entitlements() {
  # Xcode fills $(BASE_BUNDLE_IDENTIFIER) when it signs; ldid does not.
  sed "s/\$(BASE_BUNDLE_IDENTIFIER)/$bundle_id/g" "$1" > "$work/$(basename "$1")"
  echo "$work/$(basename "$1")"
}

# inside out: frameworks and the tunnel extension before the app that holds them
find "$app/Frameworks" -name '*.framework' -type d | while read -r framework; do
  ldid -S "$framework/$(basename "$framework" .framework)"
done
for appex in "$app"/PlugIns/*.appex; do
  [[ -d "$appex" ]] || continue
  name="$(basename "$appex" .appex)"
  ldid -S"$(entitlements "ios/$name/$name.entitlements")" "$appex/$name"
done
ldid -S"$(entitlements ios/Runner/Runner.entitlements)" "$app/Runner"

mkdir -p "$work/Payload" out
cp -R "$app" "$work/Payload/"
(cd "$work" && zip -qry ipa.zip Payload)
mv "$work/ipa.zip" out/Hiddify-iOS-Jailbreak.ipa
ls -la out
