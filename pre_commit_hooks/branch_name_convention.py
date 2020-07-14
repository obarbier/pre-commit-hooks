import argparse
def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )

    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    exit(main())
