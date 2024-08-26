import subprocess
import PackageManager

class Compressed():
    def __init__(self):
        self.packages= ["inetutils", "libxcrypt-compat", "net-tools"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.packages = self.packages
        self.package_manager.install_packages()

    def file(self):
        print("Xampp installing...")
        subprocess.run(["wget", "https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["chmod", "+x", "xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["sudo", "./xampp-linux-x64-8.2.12-0-installer.run"])

