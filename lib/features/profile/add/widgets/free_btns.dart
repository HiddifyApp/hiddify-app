import 'package:flutter/material.dart';
import 'package:gap/gap.dart';
import 'package:hiddify/core/localization/translations.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

/// Free configs are removed from this build: shared public servers can log and leak their users'
/// traffic. The "Free" tab only explains why.
class FreeBtns extends ConsumerWidget {
  const FreeBtns({super.key, required this.scrollController});

  final ScrollController scrollController;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final t = ref.watch(translationsProvider).requireValue;
    final theme = Theme.of(context);
    return SingleChildScrollView(
      controller: scrollController,
      padding: const EdgeInsets.all(24),
      child: Column(
        children: [
          Icon(Icons.shield_rounded, size: 40, color: theme.colorScheme.primary),
          const Gap(12),
          Text(
            t.pages.profiles.freeConfigsRemoved,
            textAlign: TextAlign.center,
            style: theme.textTheme.bodyMedium!.copyWith(color: theme.colorScheme.onSurface),
          ),
        ],
      ),
    );
  }
}
