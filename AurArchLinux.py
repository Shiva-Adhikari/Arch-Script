import os
import subprocess
import PackageManager

class AurArchLinux:
    def __init__(self):
        self.aur_packages = {
        "paru-bin": "https://aur.archlinux.org/paru-bin.git",
        "text-engine": "https://aur.archlinux.org/text-engine.git",
        "gnome-shell-extension-clipboard-indicator": "https://aur.archlinux.org/gnome-shell-extension-clipboard-indicator.git",
        "gnome-dash-fix": "https://github.com/BenJetson/gnome-dash-fix.git",
        "caprine": "https://aur.archlinux.org/caprine.git",
        "whatsie": "https://aur.archlinux.org/whatsie.git",
        "ttf-ms-fonts": "https://aur.archlinux.org/ttf-ms-fonts.git",
        "preload": "https://aur.archlinux.org/preload.git",
        "linux-wifi-hotspot": "https://aur.archlinux.org/linux-wifi-hotspot.git",
        "auto-cpufreq": "https://aur.archlinux.org/auto-cpufreq.git",
        "vscodium-bin": "https://aur.archlinux.org/vscodium-bin.git",
        "librewolf-bin": "https://aur.archlinux.org/librewolf-bin.git",
        "extension-manager": "https://aur.archlinux.org/extension-manager.git",
        "logseq-desktop-bin": "https://aur.archlinux.org/logseq-desktop-bin.git",
        }

        self.key_id = ["662E3CDD6FE329002D0CA5BB40339DD82B12EF16"]    # Librewolf key

        self.packages = ["dnsmasq", "hostapd"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.packages = self.packages       # Override the default package list
        self.package_manager.install_packages()

## this code may help me for future  # don't forget to call in main object
    # def install_packages(self):
        # package_manager = PackageManager.PackageManager()
        # package_manager.packages = self.packages
        # package_manager.install_packages()
        
        self.services = ["preload"]
        self.package_manager = PackageManager.PackageManager()
        self.package_manager.enable_packages = self.services
        self.package_manager.enable_service()


    def install_aur_packages(self):
        print(f"Installing Aur packages...")

        for package_name, package_id in self.aur_packages.items():
            query = subprocess.run(["pacman", "-Qq", package_name], capture_output=True, text=True)
            if query.returncode == 0:
                print(f"{package_name} already installed, skipping...")
                continue

            git_check = subprocess.run(["ls", package_name], capture_output=True, text=True)
            if git_check.returncode == 0:
                os.chdir(package_name)
            else:
                subprocess.run(["git", "clone", package_id])
                os.chdir(package_name)

            makepkg = subprocess.run(["ls", "PKGBUILD"], capture_output=True, text=True)
            if makepkg.returncode == 0:
                subprocess.run(["makepkg", "-si"])
                pass

            if package_name == "gnome-dash-fix":
                bashinstall = subprocess.run(["ls", "appfixer.sh"], capture_output=True, text=True)
                if bashinstall.returncode == 0:
                    subprocess.run(["chmod", "+x", "appfixer.sh"])
                    subprocess.run(["bash", "appfixer.sh"])
                
            os.chdir("..")
            subprocess.run(["rm","-rf",package_name])
            
    

    def gpg_key(self):
        for key_id in key_ids:
            check_key = subprocess.run(["gpg", "--recv-key", key_id], capture_output=True, text=True)
            if check_key.returncode == 0:
                print("Already Added gpg key")
            else:
                subprocess.run(["gpg", "--recv-key", key_id])

