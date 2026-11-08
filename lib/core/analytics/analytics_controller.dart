import 'package:hiddify/core/logger/sinks/sentry_sink.dart';

import 'package:hiddify/core/preferences/preferences_provider.dart';
import 'package:hiddify/utils/custom_loggers.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';
import 'package:sentry_flutter/sentry_flutter.dart';
import 'package:shared_preferences/shared_preferences.dart';

part 'analytics_controller.g.dart';

const String enableAnalyticsPrefKey = "enable_analytics";

bool readAnalyticsEnabled(SharedPreferences preferences) {
  return preferences.getBool(enableAnalyticsPrefKey) ?? false;
}

@Riverpod(keepAlive: true)
class AnalyticsController extends _$AnalyticsController with AppLogger {
  @override
  Future<bool> build() async {
    // Analytics are removed from this build; an old "on" from before is turned off.
    if (readAnalyticsEnabled(_preferences)) await _preferences.setBool(enableAnalyticsPrefKey, false);
    return false;
  }

  SharedPreferences get _preferences => ref.read(sharedPreferencesProvider).requireValue;

  /// Analytics are removed from this build: nothing is ever sent, so this only makes sure they stay off.
  Future<void> enableAnalytics() => disableAnalytics();

  Future<void> disableAnalytics() async {
    if (state case AsyncData()) {
      loggy.debug("disabling analytics");
      state = const AsyncLoading();
      await _preferences.setBool(enableAnalyticsPrefKey, false);
      await Sentry.close();
      logDisableSentry();
      state = const AsyncData(false);
    }
  }
}
