# Built in Module
import subprocess

# Local Module
from base import Base


class Flathub(Base):
    def __init__(self):
        self.packages = {
            "Telegram":               "org.telegram.desktop",
            "Teams":                  "com.github.IsmaelMartinez.teams_for_linux",
            "Ultimate Media Downloader": "com.ktechpit.ultimate-media-downloader",
        }

    def run(self):
        print("Installing Flathub packages using flatpak...")
        for package_name, package_id in self.packages.items():
            print(f"Installing {package_name}...")
            subprocess.run(["flatpak", "install", "flathub", "-y", package_id])
        print("Done.")
