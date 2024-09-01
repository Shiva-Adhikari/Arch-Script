import subprocess
class PackageManager:
    def __init__(self):
        self.packages = ["timeshift", "celluloid", "git", "gnome-boxes", "hostapd", "iw", "flatpak", "man", "neofetch", "p7zip", "rsync", "git", "htop", "exfat-utils", "fuse-exfat", "ntfs-3g", "flac", "jasper", "aria2", "curl", "wget", "jdk-openjdk", "intel-ucode", "base-devel", "android-tools", "acpi", "cmake", "cython", "dkms", "linux-headers", "dosfstools", "thunar", "python-pyinotify", "plocate", "inetutils", "libxcrypt-compat", "net-tools", "python-pipx", "keepassxc", "qbittorrent", "signal-desktop", "php", "gedit", "aircrack-ng", "macchanger", "yt-dlp", "jupyter-notebook", "python-scikit-learn", "python-pandas", "python-seaborn", "ffmpeg", "reflector", "noto-fonts", "hddtemp", "obs-studio", "gnome-shell-extension-dash-to-panel", "acpid", "dnsmasq","mokutil", "libreoffice-fresh", "powertop", "virtualbox-host-dkms", "virtualbox-guest-iso",
        ]

        self.enable_packages = ["acpi", "powertop"]

    def install_packages(self):
        # self.packages = packages
        print("Installing packages using Pacman...")

        for package in self.packages:
            result = subprocess.run(["pacman", "-Qq", package], capture_output=True, text=True)

            if result.returncode != 0:
                subprocess.run("clear")
                print(f"Installing {package}...")
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
            else:
                print(f"{package} already installed.")

    def enable_service(self):
# first check status if not enable run this program
        for enable_package in self.enable_packages:
## solve this line no. 14 ( double function (look down))
            result = subprocess.run(["pacman", "-Qq", enable_package], capture_output=True, text=True)
            if result.returncode == 0:
                status = subprocess.run(["systemctl", "is-enabled", enable_package], capture_output=True, text=True)
                if status.returncode == 0:
                    print(f"{enable_package} already enabled")
                else:
                    subprocess.run(["sudo", "systemctl", "enable", enable_package])
                    print(f"{enable_package} has been enabled")
            else:
                print("Please install f{enable_package} first")
