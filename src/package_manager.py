# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config, logger


class PackageManager(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["pacman"]
        self.enable_packages = config["pacman_services"]

    def run(self):
        self.install_packages()
        self.enable_service()

    def install_packages(self):
        logger.info("Installing packages using Pacman...")
        for package in self.packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode != 0:
                subprocess.run("clear")
                logger.info(f"Installing {package}...")
                result = subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
                if result.returncode != 0:
                    logger.warning(f"Failed to install {package}")
            else:
                logger.info(f"{package} already installed.")

    def enable_service(self):
        for package in self.enable_packages:
            result = self._run_cmd(["systemctl", "is-enabled", package])
            if result.returncode == 0:
                logger.info(f"{package} already enabled.")
            else:
                logger.info(f"Enabling {package}...")
                result = subprocess.run(["sudo", "systemctl", "enable", "--now", package])
                if result.returncode != 0:
                    logger.warning(f"Failed to enable {package}")
