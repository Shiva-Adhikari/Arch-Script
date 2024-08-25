import subprocess
import PackageManager
import AurArchLinux


if __name__ == '__main__':
    
    package = ["ufw"]
    package_manager = PackageManager.PackageManager()
    package_manager.install_packages(package)


    enable_packages = ["ufw"]
    aur = AurArchLinux.AurArchLinux()
    aur.enable_service(enable_packages)

