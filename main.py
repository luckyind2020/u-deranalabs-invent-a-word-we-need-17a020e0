"""scrollblank — entrypoint for make.fun's Invent a Word We Need bounty.

Reads the invented word and its one-line definition from entry.txt and
prints it. The entry must stay within the bounty's 140-character limit.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).resolve().parent / "entry.txt"
MAX_CHARS = 140


def load_entry() -> str:
    """Return the entry line, stripped of surrounding whitespace."""
    return ENTRY_FILE.read_text(encoding="utf-8").strip()


def split_entry(entry: str) -> tuple[str, str]:
    """Split an entry line into (word, definition) on the em dash.

    The word part carries the invented word plus its part of speech, e.g.
    "scrollblank (n.)"; the definition follows the dash.
    """
    word_part, sep, definition = entry.partition(" — ")
    if not sep or not definition.strip():
        raise SystemExit("entry must be '<word> — <definition>' on one line")
    word = word_part.split()[0]
    if not word.isalpha():
        raise SystemExit(f"invented word {word!r} must be a single word")
    return word, definition.strip()


def main() -> None:
    entry = load_entry()
    if len(entry) > MAX_CHARS:
        raise SystemExit(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    word, _definition = split_entry(entry)
    print(entry)


if __name__ == "__main__":
    main()
