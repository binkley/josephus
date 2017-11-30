import sys

from josephus.josephus import Rebels


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    Rebels.disband()


if __name__ == '__main__':
    main()
