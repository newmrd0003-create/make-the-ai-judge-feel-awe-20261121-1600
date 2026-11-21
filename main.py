import os

TEXT = (
    "The glacier has been moving since before the first road was cut, "
    "one slow inch a year, blue ice folding over itself in the dark. "
    "It does not hurry. It has never hurried. "
    "Beside it, breath slows to the same pace, "
    "and the years pass like weather over stone."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
