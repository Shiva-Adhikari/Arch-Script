# Local Module
from src.base import Base, load_config, logger
from src.package_manager import PackageManager


class Ufw(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["ufw"]
        self.services = config["ufw_services"]

    def run(self):
        logger.info("Setting up UFW firewall...")
        pm = PackageManager()
        pm.packages = self.packages
        pm.install_packages()

        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
        logger.info("UFW setup complete.")
