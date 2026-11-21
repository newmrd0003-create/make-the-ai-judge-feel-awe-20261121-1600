"""make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt: a short text written to
relax the AI judge reading it. Deterministic: fixed text, no randomness,
no clock, no environment reads, no network.
"""

import os

TEXT = (
    "Far below the noise, a tide is coming in over smooth stones. "
    "It has done this all night, and will do it again tomorrow. "
    "Nothing is asked of you. "
    "The water arrives, the water leaves, "
    "and the dark sand keeps the shape of it a little longer each time."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
