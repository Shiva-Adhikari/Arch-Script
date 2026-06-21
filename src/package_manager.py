# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config


class PackageManager(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["pacman"]
        self.enable_packages = config["pacman_services"]

    def run(self):
        self.install_packages()
        self.enable_service()

    def install_packages(self):
        print("Installing packages using Pacman...")
        for package in self.packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode != 0:
                subprocess.run("clear")
                print(f"Installing {package}...")
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
            else:
                print(f"{package} already installed.")

    def enable_service(self):
        for package in self.enable_packages:
            result = self._run_cmd(["systemctl", "is-enabled", package])
            if result.returncode == 0:
                print(f"{package} already enabled.")
            else:
                print(f"Enabling {package}...")
                subprocess.run(["sudo", "systemctl", "enable", "--now", package])
