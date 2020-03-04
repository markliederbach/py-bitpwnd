import sys
import click
from bitpwnd.clients import bw, hibp


@click.command()
@click.option(
    "--password",
    "-p",
    type=click.STRING,
    default=None,
    help="Check an individual password",
)
def run(password):
    if password is not None:
        pwned = hibp.HaveIBeenPwned()
        result = pwned.check_password(password)
        if result:
            click.secho(
                f"Password has been found in {result} breach{'es' if result > 1 else ''}",
                fg="red",
            )
            sys.exit(1)
        else:
            click.secho("Password is safe", fg="green")
            sys.exit(0)


if __name__ == "__main__":
    run()
