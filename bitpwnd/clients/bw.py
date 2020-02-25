import os
import logging
import subprocess

from bitpwnd import exceptions


log = logging.getLogger(__name__)


class Bitwarden:
    def __init__(self, session_token=None, bw_path=None):
        self.session_token = session_token or os.environ.get("BW_SESSION", None)
        # if self.session_token is None:
        #     raise exceptions.BitwardenException(
        #         "bw CLI requires a session token. Pass as an arg, or export BW_SESSION"
        #     )
        self.bw_path, _, _ = bw_path or self.run_command("which bw")

    def run_command(self, command, raise_for_nonzero=True):
        process = subprocess.Popen(
            command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if raise_for_nonzero and process.returncode != 0:
            newline = "\n"
            raise exceptions.BitwardenException(
                f"Command [{command}] returned non-zero exit code ({process.returncode}){newline}{stderr.decode('utf-8').rstrip(newline)}"
            )
        return (
            stdout.decode("utf-8").rstrip("\n"),
            stderr.decode("utf-8").rstrip("\n"),
            process.returncode,
        )
