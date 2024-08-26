import subprocess
import PackageManager
import AurArchLinux

class Ufw:
    def __init__(self):
        self.package = ["ufw"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager = self.package
        self.package_manager.install_packages()

if __name__ == '__main__':

    enable_packages = ["ufw"]
    aur = AurArchLinux.AurArchLinux()
    aur.enable_service(enable_packages)

