# Built in Module
import os
import subprocess

# Local Module
from src.base import Base


class Sudoers(Base):
    def __init__(self):
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.sudoers_path = "/etc/sudoers"

    def run(self):
        print(f"Adding {self.username} to sudoers...")
        lines = [
            f"\n##Bypass SUDO by {self.username}",
            f"{self.username} ALL=(ALL:ALL) NOPASSWD: ALL",
        ]
        for line in lines:
            subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> {self.sudoers_path}"])
        print("Done.")
