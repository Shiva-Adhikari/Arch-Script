import subprocess
class Uninstall:
    def __init__(self):
        self.packages = ["gnome-maps", "gnome-music", "gnome-tour", "gnome-weather"]

    def remove_packages(self):
        print("Removing packages using Pacman...")
        for package in self.packages:
            result = subprocess.run(["pacman", "-Qq", package], capture_output=True, text=True)
            if result.returncode == 0:
                subprocess.run("clear")
                print(f"Removing {package}...")
                subprocess.run(["sudo", "pacman", "-Rn", "--noconfirm", package])
            else:
                print(f"{package} is already Removed.")

