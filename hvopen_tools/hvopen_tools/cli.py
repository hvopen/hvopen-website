# -*- coding: utf-8 -*-

"""Console script for hvopen_tools."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for hvopen_tools."""
    click.echo("Replace this message by putting your code into "
               "hvopen_tools.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
