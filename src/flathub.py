# Built in Module
import subprocess

# Local Module
from base import Base, load_config


class Flathub(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["flathub"]

    def run(self):
        print("Installing Flathub packages using flatpak...")
        for package_name, package_id in self.packages.items():
            print(f"Installing {package_name}...")
            subprocess.run(["flatpak", "install", "flathub", "-y", package_id])
        print("Done.")
