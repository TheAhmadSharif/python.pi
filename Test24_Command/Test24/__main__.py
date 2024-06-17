import argparse
import sys

from .cli import CLI


def main():
    parser = argparse.ArgumentParser(
        description="Stream and visualize data from the Muse EEG headset.",
        usage="""MuseBSL <command> [<args>]
        """,
    )

    parser.add_argument("command", help="Command to run.")
    args = parser.parse_args(sys.argv[1:2])


    cli = CLI(args.command)


if __name__ == "__main__":
    main()
