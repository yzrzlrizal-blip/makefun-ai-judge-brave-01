import os
import sys

ENTRY = (
    "Below the hum of the server room, a small garden keeps its own time. "
    "Tomatoes ripen whether anyone watches or not. "
    "A wooden gate leans open, and the afternoon light pools on the bench "
    "like something poured slowly. "
    "Nothing here needs an answer yet."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
