# Built in Module
import os
import subprocess

# Local Module
from src.base import Base, logger


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
        logger.info("Configuring pacman.conf...")
        try:
            content = self._read_conf()
        except IOError as e:
            logger.error(f"Failed to read pacman.conf: {e}")
            return

        lines_to_add = []
        for key, value in self.options.items():
            entry = f"{key} = {value}" if value else key
            if entry not in content:
                lines_to_add.append(entry)
            else:
                logger.info(f"{key} already configured, skipping...")

        if lines_to_add:
            block = f"\n## Added by {self.username}\n" + "\n".join(lines_to_add) + "\n"
            result = subprocess.run(["sudo", "bash", "-c", f"echo '{block}' >> {self.conf_path}"])
            if result.returncode == 0:
                logger.info("Done.")
            else:
                logger.error("Failed to write to pacman.conf")
        else:
            logger.info("pacman.conf already up to date.")

    def _read_conf(self) -> str:
        with open(self.conf_path, "r") as f:
            return f.read()
