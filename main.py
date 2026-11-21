import os

TEXT = """Before dawn your grandmother
is already kneading dough.
The flour is warm from her hands.

She folds it over,
and over again.
The wheat grew in a summer
before you were born.

You sit on the warm floor
and watch the oven glow.
The bread will rise
while you sleep."""

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
