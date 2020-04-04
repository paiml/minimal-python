import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', is_flag=True, help='Produce more output')
@click.pass_context
def main(ctx, verbose):
    """ A Tool that deals with filesystems """
    return

@main.command()
@click.argument('size')
def zfs(size):
    pass

@main.command()
@click.argument('size', type=int)
@click.pass_context
def lvm(ctx, size):
    print('Parent params: %s' % ctx.parent.params)
    print('Current params: %s' % ctx.params)

if __name__ == '__main__':
    main()

#def main():
#    parser = argparse.ArgumentParser(
#        description="A tool that deals with filesystems"
#    )
#
#    parser.add_argument('--verbose', action='store_true', help='Produce more output')
#
#
#    subparsers = parser.add_subparsers(help='Filesystem sub-commands')
#
#    # LVM sub-command
#    lvm_parser = subparsers.add_parser('lvm', help='The LVM sub-command')
#    lvm_parser.add_argument('size', type=int, help='The size to work with')
#
#    # ZFS sub-command
#    zfs_parser = subparsers.add_parser('zfs', help='The ZFS sub-command')
#    zfs_parser.add_argument('size', type=int, help='The size to work with')
#
#    parser.parse_args()
#
#
#if __name__ == '__main__':
#    main()
