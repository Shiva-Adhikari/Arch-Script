# Built in Module
import os
import subprocess

# Local Module
from src.base import Base, logger


class Sudoers(Base):
    def __init__(self):
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.sudoers_path = "/etc/sudoers"
        self.entry = f"{self.username} ALL=(ALL:ALL) NOPASSWD: ALL"

    def run(self):
        content = self._read_sudoers()
        if self.entry in content:
            logger.info(f"{self.username} already in sudoers, skipping...")
            return

        logger.info(f"Adding {self.username} to sudoers...")
        lines = [
            f"\n## Bypass SUDO by {self.username}",
            self.entry,
        ]
        for line in lines:
            result = subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> {self.sudoers_path}"])
            if result.returncode != 0:
                logger.error(f"Failed to write to sudoers: {line}")
                return
        logger.info("Done.")

    def _read_sudoers(self) -> str:
        result = subprocess.run(["sudo", "cat", self.sudoers_path], capture_output=True, text=True)
        return result.stdout
