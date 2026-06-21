# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config, logger


class Uninstall(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["uninstall"]

    def run(self):
        logger.info(f"This will remove: {', '.join(self.packages)}")
        confirm = input("Continue? (yes/no): ").strip().lower()
        if confirm != "yes":
            logger.info("Aborted.")
            return

        logger.info("Removing packages using Pacman...")
        for package in self.packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode == 0:
                subprocess.run("clear")
                logger.info(f"Removing {package}...")
                result = subprocess.run(["sudo", "pacman", "-Rn", "--noconfirm", package])
                if result.returncode != 0:
                    logger.warning(f"Failed to remove {package}")
            else:
                logger.info(f"{package} is already removed.")
