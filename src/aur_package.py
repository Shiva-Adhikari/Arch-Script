# Built in Module
import os
import subprocess

# Local Module
from base import Base
from package_manager import PackageManager


class AurPackage(Base):
    def __init__(self):
        self.aur_packages = {
            "paru-bin":                                     "https://aur.archlinux.org/paru-bin.git",
            "text-engine":                                  "https://aur.archlinux.org/text-engine.git",
            "gnome-shell-extension-clipboard-indicator":    "https://aur.archlinux.org/gnome-shell-extension-clipboard-indicator.git",
            "gnome-dash-fix":                               "https://github.com/BenJetson/gnome-dash-fix.git",
            "caprine":                                      "https://aur.archlinux.org/caprine.git",
            "whatsie":                                      "https://aur.archlinux.org/whatsie.git",
            "ttf-ms-fonts":                                 "https://aur.archlinux.org/ttf-ms-fonts.git",
            "preload":                                      "https://aur.archlinux.org/preload.git",
            "linux-wifi-hotspot":                           "https://aur.archlinux.org/linux-wifi-hotspot.git",
            "auto-cpufreq":                                 "https://aur.archlinux.org/auto-cpufreq.git",
            "vscodium-bin":                                 "https://aur.archlinux.org/vscodium-bin.git",
            "librewolf-bin":                                "https://aur.archlinux.org/librewolf-bin.git",
            "extension-manager":                            "https://aur.archlinux.org/extension-manager.git",
            "logseq-desktop-bin":                           "https://aur.archlinux.org/logseq-desktop-bin.git",
        }

        self.gpg_keys = ["662E3CDD6FE329002D0CA5BB40339DD82B12EF16"]  # Librewolf key

        self.dependencies = ["dnsmasq", "hostapd"]
        self.services = ["preload"]

    def run(self):
        self._install_dependencies()
        self._import_gpg_keys()
        self._install_aur_packages()
        self._enable_services()

    def _install_dependencies(self):
        pm = PackageManager()
        pm.packages = self.dependencies
        pm.install_packages()

    def _import_gpg_keys(self):
        for key in self.gpg_keys:
            print(f"Importing GPG key: {key}")
            subprocess.run(["gpg", "--recv-key", key])

    def _install_aur_packages(self):
        print("Installing AUR packages...")
        for package_name, package_url in self.aur_packages.items():
            result = self._run_cmd(["pacman", "-Qq", package_name])
            if result.returncode == 0:
                print(f"{package_name} already installed, skipping...")
                continue

            if not os.path.exists(package_name):
                subprocess.run(["git", "clone", package_url])

            os.chdir(package_name)

            if os.path.exists("PKGBUILD"):
                subprocess.run(["makepkg", "-si"])
            elif package_name == "gnome-dash-fix" and os.path.exists("appfixer.sh"):
                subprocess.run(["chmod", "+x", "appfixer.sh"])
                subprocess.run(["bash", "appfixer.sh"])

            os.chdir("..")
            subprocess.run(["rm", "-rf", package_name])

    def _enable_services(self):
        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
