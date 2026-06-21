# Built in Module
import subprocess


class Base:
    def run(self):
        raise NotImplementedError("Subclasses must implement run()")

    def _run_cmd(self, cmd: list) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, capture_output=True, text=True)

    def _run_sudo(self, cmd: list) -> subprocess.CompletedProcess:
        return subprocess.run(["sudo"] + cmd)
