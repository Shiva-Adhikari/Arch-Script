# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config
from src.package_manager import PackageManager


class Bluetooth(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["bluetooth"]
        self.services = config["bluetooth_services"]

    def run(self):
        pm = PackageManager()
        pm.packages = self.packages
        pm.install_packages()

        subprocess.run(["sudo", "modprobe", "btusb"])

        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
