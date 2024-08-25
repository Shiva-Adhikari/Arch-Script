import subprocess

class FlathubManager:
    def __init__(self, flathub_packages):
        self.flathub_packages = flathub_packages

    def install_flathub_packages(self):
        print("Installing Flathub packages using flatpak...")
        
        for package_name, package_id in self.flathub_packages.items():
             print(f"Installing {package_name}...")
             subprocess.run(["flatpak", "install", "flathub", "-y", package_id])

if __name__ == '__main__':
    flathub_packages = {
    "Telegram": "org.telegram.desktop",
    "Teams": "com.github.IsmaelMartinez.teams_for_linux",
    "Ultimate Media Downloader": "com.ktechpit.ultimate-media-downloader",
    "LibreOffice": "org.libreoffice.LibreOffice",
    }

    flathub_manager = FlathubManager(flathub_packages)
    flathub_manager.install_flathub_packages()
