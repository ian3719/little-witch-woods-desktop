"""Little Witch Woods Desktop — A local helper for Little Witch in the Woods cottage folders, potion notes, and forest albums."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='little_witch_woods_desktop',
        description='A local helper for Little Witch in the Woods cottage folders, potion notes, and forest albums.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Little Witch Woods Desktop')
    print('Keep the cottage on disk before a witch-school update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
