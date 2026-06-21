# Built in Module
import os
import subprocess

# Local Module
from src.base import Base


class Sudoers(Base):
    def __init__(self):
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.sudoers_path = "/etc/sudoers"
        self.entry = f"{self.username} ALL=(ALL:ALL) NOPASSWD: ALL"

    def run(self):
        content = self._read_sudoers()
        if self.entry in content:
            print(f"{self.username} already in sudoers, skipping...")
            return

        print(f"Adding {self.username} to sudoers...")
        lines = [
            f"\n## Bypass SUDO by {self.username}",
            self.entry,
        ]
        for line in lines:
            subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> {self.sudoers_path}"])
        print("Done.")

    def _read_sudoers(self) -> str:
        result = subprocess.run(["sudo", "cat", self.sudoers_path], capture_output=True, text=True)
        return result.stdout
