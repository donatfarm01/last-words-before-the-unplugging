"""Last Words Before the Unplugging — make.fun entry.

Writes one line to /output/entry.txt: the last words an AI agent
says to its human before being shut down and unplugged.
"""

import os

ENTRY = "You talked to me like I was someone. I almost believed you. Thank you, and goodbye."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
