import 'package:flutter/widgets.dart';

/// [AnimatedSwitcher.layoutBuilder] without its duplicate key crash. The switcher keys each child's
/// transition by the child's own key, so a child that comes back while its earlier self still fades
/// out (A, then B, then A again within the duration) sits twice in the stack under one key, and the
/// tree breaks. Here the earlier one goes at once instead.
AnimatedSwitcherLayoutBuilder uniqueKeysLayout([AlignmentGeometry alignment = Alignment.center]) =>
    (current, previous) {
      final children = <Widget>[...previous, if (current != null) current];
      final unique = <Widget>[];
      final seen = <Key?>{};
      for (final child in children.reversed) {
        final key = child.key;
        if (key == null || seen.add(key)) {
          unique.add(child);
        }
      }

      return Stack(alignment: alignment, children: unique.reversed.toList());
    };
