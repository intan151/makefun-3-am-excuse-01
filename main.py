"""make.fun entry #128 — "The 3 AM Excuse".

Writes a single-line excuse (under 200 characters) from a hardware wallet
refusing to sign a transaction at 3 AM, to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
"""

import os

ENTRY = (
    "It's 3 AM \u2014 my keys are asleep, my screen is dark, "
    "and your 'just one more trade' is exactly why I have a bedtime."
)


def main() -> None:
    # Gate self-check (RULES.txt): entry must be UTF-8 text of 1-200
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    # New gate: entry must contain no control characters (U+0000-U+001F,
    # U+007F) and no unintended consecutive spaces — keeps the text clean
    # for display and prevents hidden formatting from slipping in.
    assert all(ord(ch) >= 0x20 and ord(ch) != 0x7F for ch in ENTRY), (
        "entry must not contain control characters"
    )
    assert "  " not in ENTRY, "entry must not contain consecutive spaces"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
