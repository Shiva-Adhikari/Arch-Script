# Built in Module
import os
import subprocess
import tempfile

# Local Module
from src.base import Base, logger


class BlackArch(Base):
    def __init__(self):
        self.mirrorlist = "/etc/pacman.d/blackarch-mirrorlist"
        self.strap_url = "https://blackarch.org/strap.sh"

    def run(self):
        if os.path.exists(self.mirrorlist):
            logger.info("BlackArch already installed.")
            return

        logger.info("Installing BlackArch...")
        subprocess.run(["sudo", "pacman", "-Syu"])

        result = subprocess.run(["sudo", "pacman", "-S", "curl", "--noconfirm"])
        if result.returncode != 0:
            logger.error("Failed to install curl.")
            return

        with tempfile.TemporaryDirectory() as tmpdir:
            strap_path = os.path.join(tmpdir, "strap.sh")
            result = subprocess.run(["curl", "-o", strap_path, self.strap_url])
            if result.returncode != 0:
                logger.error("Failed to download strap.sh.")
                return

            subprocess.run(["chmod", "+x", strap_path])
            result = subprocess.run(["sudo", strap_path])
            if result.returncode != 0:
                logger.error("Failed to run strap.sh.")
                return

        logger.info("BlackArch installed.")
