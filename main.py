"""Prompt Library Local — Store reusable prompt snippets in a local folder and copy one to the clipboard by name."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='prompt_library_local',
        description='Store reusable prompt snippets in a local folder and copy one to the clipboard by name.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Prompt Library Local')
    print('Your prompts as files, not a chat history.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
