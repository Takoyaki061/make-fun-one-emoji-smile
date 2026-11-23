#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty entry.

Writes a single emoji to /output/entry.txt: heart hands (U+1FAF6).

Why this one, from five DeepSeek-brainstormed candidates (sunflower,
sun-behind-cloud, coffee, heart hands, puppy) judged against the kit's
criteria in order:
  1. Warm at first glance — two hands shaping a heart is warmth itself,
     not a symbol of it (sunflower, coffee) and not weather (sun-cloud).
  2. Universal — a gesture of care needs no language, no in-joke, and
     no shared context; a puppy is cute but says "cute", not "kind".
  3. Chosen, not default — it is a deliberate offer, not the first
     smiley that comes to mind, yet still instantly readable.
  4. Right for a stranger — an offered heart is friendly without
     intimacy, sarcasm or flirtation; a hug face would read too close.
"""

import os

EMOJI = "\U0001faf6"  # 🫶 heart hands


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
