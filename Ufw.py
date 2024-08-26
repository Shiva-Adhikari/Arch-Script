import subprocess
import PackageManager

class Ufw:
    def __init__(self):
        self.package = ["ufw"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.packages = self.package
        self.package_manager.install_packages()

        self.packages = ["ufw"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.enable_packages = self.packages
        self.package_manager.enable_service()

