from typing import AbstractSet
import re
import argparse
from typing import AbstractSet
from typing import Optional
from typing import Sequence
from typing import Set

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def is_on_branch(
    patterns: AbstractSet[str] = frozenset(),
) -> bool:
    try:
        # git branch --show-current
        branch_name = cmd_output('git', 'branch', '--show-current')
    except CalledProcessError:  # pragma: no cover (with git-lfs)
        return False
    for p in patterns:
        if re.match(p, branch_name) is not None:
            return True
    return False


def main(argv: Sequence[str] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--pattern', action='append',
        help=(
            'regex pattern for branch name to disallow commits to, '
            'may be specified multiple times'
        ),
    )
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    patterns = frozenset(args.pattern or ())
    return int(is_on_branch(patterns))


if __name__ == '__main__':
    exit(main())
