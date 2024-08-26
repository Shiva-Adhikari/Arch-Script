import subprocess
import PackageManager

class Bluetooth():
    def __init__(self):
# install package
        self.packages = ["bluez", "blueman", "bluez-utils"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.packages = self.packages
        self.package_manager.install_packages()
# add
        subprocess.run(["sudo", "modprobe", "btusb"])

        self.package = ["bluetooth"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.enable_packages = self.package
        self.package_manager.enable_service()

