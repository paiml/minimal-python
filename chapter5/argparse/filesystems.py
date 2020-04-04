import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A tool that deals with filesystems"
    )

    parser.add_argument('--verbose', action='store_true', help='Produce more output')


    subparsers = parser.add_subparsers(help='Filesystem sub-commands')

    # LVM sub-command
    lvm_parser = subparsers.add_parser('lvm', help='The LVM sub-command')
    lvm_parser.add_argument('size', type=int, help='The size to work with')

    # ZFS sub-command
    zfs_parser = subparsers.add_parser('zfs', help='The ZFS sub-command')
    zfs_parser.add_argument('size', type=int, help='The size to work with')

    parser.parse_args()


if __name__ == '__main__':
    main()
