import os
import sys
import pytest


def main():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)

    args = ['--reruns', '1', '--alluredir=' + './report/result/']
    pytest.main(args)


if __name__ == '__main__':
    main()
