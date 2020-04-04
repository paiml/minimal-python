import argparse


def main():
    parser = argparse.ArgumentParser(
        description='My first command-line tool, it handles arguments and values'
    )
    parser.parse_args()


if __name__ == '__main__':
    main()
