# Built in Module
import subprocess

# Local Module
from src.base import Base, load_config


class Uninstall(Base):
    def __init__(self):
        config = load_config()
        self.packages = config["uninstall"]

    def run(self):
        print(f"This will remove: {', '.join(self.packages)}")
        confirm = input("Continue? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Aborted.")
            return

        print("Removing packages using Pacman...")
        for package in self.packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode == 0:
                subprocess.run("clear")
                print(f"Removing {package}...")
                result = subprocess.run(["sudo", "pacman", "-Rn", "--noconfirm", package])
                if result.returncode != 0:
                    print(f"Warning: failed to remove {package}")
            else:
                print(f"{package} is already removed.")
