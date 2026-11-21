import os

TEXT = """You hang in blue water,
weightless, and below you
the dark goes down
farther than any rope
could reach.

A fish passes,
slow as a thought.

The sea was here
before the first shore,
before the first name
for blue.

You breathe out.
A silver thread rises
and does not hurry."""

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
