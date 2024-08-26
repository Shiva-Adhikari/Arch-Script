import subprocess
import PackageManager
import AurArchLinux

class Bluetooth():
    def __init__(self):
        self.packages = ["bluez", "blueman", "bluez-utils"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.packages = self.packages
        self.package_manager.install_packages()
        subprocess.run(["sudo", "modprobe", "btusb"])


if __name__ == '__main__':
    bluetooth = Bluetooth()

    enable_packages = ["bluetooth"]
    aur = AurArchLinux.AurArchLinux()
    aur.enable_service(enable_packages)

