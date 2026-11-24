"""The One-Line Exit -- make.fun entry.

One funny single-line resignation letter, 140 characters or fewer: the
printer and the writer have agreed the writer is the problem, and the
printer has seniority. The program checks the line, prints it, and
writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I resign, effective immediately -- mostly because the printer and I "
    "have agreed I am the problem, and it has seniority."
)

LIMIT = 140
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """A resignation letter opens with the resignation and names the printer."""
    if not line.startswith("I resign"):
        raise ValueError("letter must open with 'I resign'")
    if "printer" not in line:
        raise ValueError("letter must blame the printer")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
