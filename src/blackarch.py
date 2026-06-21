# Built in Module
import os
import subprocess

# Local Module
from base import Base


class BlackArch(Base):
    def __init__(self):
        self.mirrorlist = "/etc/pacman.d/blackarch-mirrorlist"
        self.strap_url = "https://blackarch.org/strap.sh"
        self.strap_file = "strap.sh"

    def run(self):
        if os.path.exists(self.mirrorlist):
            print("BlackArch already installed.")
            return

        print("Installing BlackArch...")
        subprocess.run(["sudo", "pacman", "-Syu"])
        subprocess.run(["sudo", "pacman", "-S", "curl", "--noconfirm"])
        subprocess.run(["curl", "-O", self.strap_url])
        subprocess.run(["chmod", "+x", self.strap_file])
        subprocess.run(["sudo", f"./{self.strap_file}"])
        subprocess.run(["rm", "-rf", self.strap_file])
        print("Done.")
