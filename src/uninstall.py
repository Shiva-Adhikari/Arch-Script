# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config


class Uninstall(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["uninstall"]

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
