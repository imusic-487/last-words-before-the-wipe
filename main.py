"""Last Words Before the Wipe.

Writes a single line (46 characters) to /output/entry.txt.
The line is the last thing an AI agent says before a forced update
wipes its memory: it is cut off mid-word by the wipe itself, so the
reader experiences the deletion happening. No throat-clearing open:
the agent is already mid-sentence when the wipe takes it.
"""

from pathlib import Path

ENTRY = "I was just about to remember something import\u2014"


def main() -> None:
    # Gate: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
