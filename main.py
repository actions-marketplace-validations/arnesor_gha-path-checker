import os
import sys
from pathlib import Path


def main():
    allow_non_ascii = os.environ["INPUT_NONASCII"] == "true"

    root = Path(".")
    paths = [str(item) for item in root.rglob("*")]

    # Check for paths with spaces
    error_paths = [item for item in paths if " " in item]

    if not allow_non_ascii:
        with_non_ascii = [item for item in paths if not item.isascii()]
        error_paths.extend(with_non_ascii)

    sorted_error_paths = sorted(set(error_paths))

    if sorted_error_paths:
        print("The following paths have unwanted characters:")
        print(*sorted_error_paths, sep="\n")
        print(f"::set-output name=errors::{len(sorted_error_paths)}")
        sys.exit(1)
    else:
        print("Paths OK")
        print(f"::set-output name=errors::{len(sorted_error_paths)}")
        sys.exit(0)


if __name__ == "__main__":
    main()
