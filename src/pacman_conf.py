# Built in Module
import os
import subprocess

# Local Module
from base import Base


class PacmanConf(Base):
    def __init__(self):
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.conf_path = "/etc/pacman.conf"
        self.options = {
            "ParallelDownloads": "10",
            "ILoveCandy": None,
            "Color": None,
        }

    def run(self):
        print("Configuring pacman.conf...")
        lines = [
            "\n",
            "[options]",
            f"## Added by {self.username}",
        ]
        for key, value in self.options.items():
            lines.append(f"{key} = {value}" if value else key)

        for line in lines:
            subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> {self.conf_path}"])
        print("Done.")
