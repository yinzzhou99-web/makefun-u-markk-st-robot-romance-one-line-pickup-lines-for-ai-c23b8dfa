"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to /output/entry.txt. Stdlib only,
no network, deterministic: the same line every run.
"""

import os
from pathlib import Path

LINE = "Are you a transformer? Because ever since I met you, my attention has been all on you."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
