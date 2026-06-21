# Built in Module
import json
import os
import subprocess

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "packages.json")


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)


class Base:
    def run(self):
        raise NotImplementedError("Subclasses must implement run()")

    def _run_cmd(self, cmd: list) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, capture_output=True, text=True)

    def _run_sudo(self, cmd: list) -> subprocess.CompletedProcess:
        return subprocess.run(["sudo"] + cmd)
