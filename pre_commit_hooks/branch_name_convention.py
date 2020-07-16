
import re 
import argparse
from typing import Optional
from typing import Sequence
from typing import Set

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def current_branch_name() -> Set[str]:
    try:
        # git branch --show-current
        branch = cmd_output('git', 'branch', '--show-current')
    except CalledProcessError:  # pragma: no cover (with git-lfs)
        branch = 'master'
    return branch


def main(argv: Optional[str] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', help='Pattern to check')
    args = parser.parse_args(argv)
    cBranch = current_branch_name()
    if re.match(args.pattern, cBranch) is not None:
        return 0
    return 1


if __name__ == '__main__':
    exit(main())
