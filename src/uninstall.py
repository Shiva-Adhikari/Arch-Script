# Built in Module
import subprocess

# Local Module
from base import Base


class Uninstall(Base):
    def __init__(self):
        self.packages = [
            "gnome-maps", "gnome-music", "gnome-tour", "gnome-weather"
        ]

    def run(self):
        print("Removing packages using Pacman...")
        for package in self.packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode == 0:
                subprocess.run("clear")
                print(f"Removing {package}...")
                subprocess.run(["sudo", "pacman", "-Rn", "--noconfirm", package])
            else:
                print(f"{package} is already removed.")
