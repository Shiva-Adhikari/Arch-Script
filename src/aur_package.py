# Built in Module
import os
import subprocess

# Local Module
from base import Base, load_config
from package_manager import PackageManager


class AurPackage(Base):
    def __init__(self):
        config = load_config()
        self.aur_packages = config["aur"]
        self.gpg_keys = config["aur_gpg_keys"]
        self.dependencies = config["aur_dependencies"]
        self.services = config["aur_services"]

    def run(self):
        self._install_dependencies()
        self._import_gpg_keys()
        self._install_aur_packages()
        self._enable_services()

    def _install_dependencies(self):
        pm = PackageManager()
        pm.packages = self.dependencies
        pm.install_packages()

    def _import_gpg_keys(self):
        for key in self.gpg_keys:
            print(f"Importing GPG key: {key}")
            subprocess.run(["gpg", "--recv-key", key])

    def _install_aur_packages(self):
        print("Installing AUR packages...")
        for package_name, package_url in self.aur_packages.items():
            result = self._run_cmd(["pacman", "-Qq", package_name])
            if result.returncode == 0:
                print(f"{package_name} already installed, skipping...")
                continue

            if not os.path.exists(package_name):
                subprocess.run(["git", "clone", package_url])

            os.chdir(package_name)

            if os.path.exists("PKGBUILD"):
                subprocess.run(["makepkg", "-si"])
            elif package_name == "gnome-dash-fix" and os.path.exists("appfixer.sh"):
                subprocess.run(["chmod", "+x", "appfixer.sh"])
                subprocess.run(["bash", "appfixer.sh"])

            os.chdir("..")
            subprocess.run(["rm", "-rf", package_name])

    def _enable_services(self):
        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
