# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config, logger


class Flathub(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["flathub"]

    def run(self):
        logger.info("Installing Flathub packages using flatpak...")
        for package_name, package_id in self.packages.items():
            logger.info(f"Installing {package_name}...")
            result = subprocess.run(["flatpak", "install", "flathub", "-y", package_id])
            if result.returncode != 0:
                logger.warning(f"Failed to install {package_name}")
        logger.info("Done.")
