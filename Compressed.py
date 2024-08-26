import subprocess
import PackageManager

class Compressed():
    def file(self):
        print("Xampp installing...")
        subprocess.run(["wget", "https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["chmod", "+x", "xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["sudo", "./xampp-linux-x64-8.2.12-0-installer.run"])

if __name__ == "__main__":
    pacman_packages= ["inetutils", "libxcrypt-compat", "net-tools"]
    package_manager = PackageManager.PackageManager()
    package_manager.install_packages(pacman_packages)

    compressed = Compressed()
    compressed.file()

    
    
