# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config, logger
from src.package_manager import PackageManager


class Bluetooth(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["bluetooth"]
        self.services = config["bluetooth_services"]

    def run(self):
        logger.info("Setting up Bluetooth...")
        pm = PackageManager()
        pm.packages = self.packages
        pm.install_packages()

        logger.info("Loading btusb module...")
        result = subprocess.run(["sudo", "modprobe", "btusb"])
        if result.returncode != 0:
            logger.warning("Failed to load btusb module.")

        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
        logger.info("Bluetooth setup complete.")
