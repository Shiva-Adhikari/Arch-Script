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
        self.paru_url = "https://aur.archlinux.org/paru-bin.git"

    def run(self):
        self._install_dependencies()
        self._import_gpg_keys()
        self._install_paru()
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

    def _install_paru(self):
        result = self._run_cmd(["pacman", "-Qq", "paru-bin"])
        if result.returncode == 0:
            print("paru already installed, skipping...")
            return

        print("Installing paru...")
        subprocess.run(["git", "clone", self.paru_url])
        os.chdir("paru-bin")
        subprocess.run(["makepkg", "-si"])
        os.chdir("..")
        subprocess.run(["rm", "-rf", "paru-bin"])
        print("paru installed.")

    def _install_aur_packages(self):
        print("Installing AUR packages...")
        for package in self.aur_packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode == 0:
                print(f"{package} already installed, skipping...")
                continue

            print(f"Installing {package}...")
            subprocess.run(["paru", "-S", "--noconfirm", package])

    def _enable_services(self):
        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
