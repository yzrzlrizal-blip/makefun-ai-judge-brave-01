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
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        print(
            "error: entry text must be 1-280 characters and not only whitespace "
            f"(got {len(ENTRY)} characters)",
            file=sys.stderr,
        )
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
