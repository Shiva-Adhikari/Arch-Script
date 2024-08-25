import subprocess
import PackageManager
import AurArchLinux

class Bluetooth():
    def enable_bluetooth(self):
        subprocess.run(["sudo", "modprobe", "btusb"])


if __name__ == '__main__':

    packages = ["bluez", "blueman", "bluez-utils"]
    package_manager = PackageManager.PackageManager()
    package_manager.install_packages(packages)

    bluetooth = Bluetooth()
    bluetooth.enable_bluetooth()

    enable_packages = ["bluetooth"]
    aur = AurArchLinux.AurArchLinux()
    aur.enable_service(enable_packages)

