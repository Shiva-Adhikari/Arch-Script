# Built in Module
import subprocess

# Local Module
from base import Base


class PackageManager(Base):
    def __init__(self):
        self.packages = [
            "timeshift", "celluloid", "git", "gnome-boxes", "hostapd", "iw",
            "flatpak", "man", "neofetch", "p7zip", "rsync", "htop",
            "exfat-utils", "fuse-exfat", "ntfs-3g", "flac", "jasper", "aria2",
            "curl", "wget", "jdk-openjdk", "intel-ucode", "base-devel",
            "android-tools", "acpi", "cmake", "cython", "dkms",
            "linux-headers", "dosfstools", "thunar", "python-pyinotify",
            "plocate", "inetutils", "libxcrypt-compat", "net-tools",
            "python-pipx", "keepassxc", "qbittorrent", "signal-desktop",
            "php", "gedit", "aircrack-ng", "macchanger", "yt-dlp",
            "jupyter-notebook", "python-scikit-learn", "python-pandas",
            "python-seaborn", "ffmpeg", "reflector", "noto-fonts", "hddtemp",
            "obs-studio", "gnome-shell-extension-dash-to-panel", "acpid",
            "dnsmasq", "mokutil", "libreoffice-fresh", "powertop",
            "virtualbox-host-dkms", "virtualbox-guest-iso"
        ]
        self.enable_packages = ["acpid", "powertop"]

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
