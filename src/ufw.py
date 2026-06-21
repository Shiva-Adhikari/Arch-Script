# Local Module
from base import Base
from package_manager import PackageManager


class Ufw(Base):
    def __init__(self):
        self.packages = ["ufw"]
        self.services = ["ufw"]

    def run(self):
        pm = PackageManager()
        pm.packages = self.packages
        pm.install_packages()

        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
