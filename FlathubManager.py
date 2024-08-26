import subprocess

class FlathubManager:
    def __init__(self):
        self.flathub_packages = {
        "Telegram": "org.telegram.desktop",
        "Teams": "com.github.IsmaelMartinez.teams_for_linux",
        "Ultimate Media Downloader": "com.ktechpit.ultimate-media-downloader",
        }


    def install_flathub_packages(self):
        print("Installing Flathub packages using flatpak...")
        
        for package_name, package_id in self.flathub_packages.items():
             print(f"Installing {package_name}...")
             subprocess.run(["flatpak", "install", "flathub", "-y", package_id])

