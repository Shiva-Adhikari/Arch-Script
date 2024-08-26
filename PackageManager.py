import subprocess
class PackageManager:
    def __init__(self):
        self.packages = ["timeshift", "celluloid", "git", "gnome-boxes", "hostapd", "iw", "flatpak", "man", "neofetch", "p7zip", "rsync", "git", "htop", "exfat-utils", "fuse-exfat", "ntfs-3g", "flac", "jasper", "aria2", "curl", "wget", "jdk-openjdk", "intel-ucode", "base-devel", "android-tools", "acpi", "cmake", "cython", "dkms", "linux-headers", "dosfstools", "thunar", "python-pyinotify", "plocate", "inetutils", "libxcrypt-compat", "net-tools", "python-pipx", "keepassxc", "qbittorrent", "signal-desktop", "php", "gedit", "aircrack-ng", "macchanger", "yt-dlp", "jupyter-notebook", "python-scikit-learn", "python-pandas", "python-seaborn", "ffmpeg", "reflector", "noto-fonts", "hddtemp", "obs-studio", "gnome-shell-extension-dash-to-panel", "acpid", "dnsmasq","mokutil", "libreoffice-fresh", "powertop", ]

    def install_packages(self):
        # self.packages = packages
        print("Installing packages using Pacman...")

        for package in self.packages:
            result = subprocess.run(["pacman", "-Q", package], capture_output=True, text=True)

            if result.returncode!= 0:
                subprocess.run("clear")
                print(f"Installing {package}...")
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
            else:
                print(f"{package} is already installed.")


if __name__ == '__main__':
    package_manager = PackageManager()
    package_manager.install_packages()


