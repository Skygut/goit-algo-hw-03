import argparse
import shutil

from pathlib import Path


def catch_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except PermissionError as er:
            print(f"Access denied: {er.filename}.")

    return inner


@catch_error
def copy_dir(source_path: Path, output_path: Path):
    for el in source_path.iterdir():
        if el.is_dir():
            copy_dir(el, output_path)
        else:
            file_suffix = el.suffix
            output_dir = None

            if not file_suffix:
                output_dir = output_path / "other"
            else:
                output_dir = output_path / file_suffix[1:]

            if output_dir.exists():
                shutil.copy(el, output_dir)
            else:
                output_dir.mkdir()
                shutil.copy(el, output_dir)


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", type=Path, required=True)
    parser.add_argument("-o", "--output", type=Path, default=Path("dist"))
    return parser.parse_args()


def main():
    args = parse_argv()
    source: Path = args.source
    output: Path = args.output

    if not source.is_dir():
        print(f"Source must be dir.")
        return

    if output.name == "dist" and not output.exists():
        output.mkdir()

    if not output.is_dir():
        print(f"Output must be dir.")
        return

    copy_dir(source, output)


if __name__ == "__main__":
    main()
