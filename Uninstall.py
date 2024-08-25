import subprocess
class PackageManager:
    def remove_packages(self, packages):
        self.packages = packages
        print("Removing packages using Pacman...")
        for package in self.packages:
            result = subprocess.run(["pacman", "-Qq", package], capture_output=True, text=True)
            if result.returncode == 0:
                subprocess.run("clear")
                print(f"Removing {package}...")
                subprocess.run(["sudo", "pacman", "-Rn", "--noconfirm", package])
            else:
                print(f"{package} is already Removed.")

if __name__ == '__main__':
    pacman_packages = ["gnome-maps", "gnome-music", "gnome-tour", "gnome-weather"]
    
    package_manager = PackageManager()
    package_manager.remove_packages(pacman_packages)
