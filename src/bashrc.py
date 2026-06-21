# Built in Module
import os
import subprocess

# Local Module
from base import Base


class Bashrc(Base):
    def __init__(self):
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.home = os.path.expanduser("~")
        self.bashrc_path = f"{self.home}/.bashrc"

        self.aliases = {
            "s":        "sensors",
            "py":       "python",
            "search":   "pacman -Ss",
            "install":  "sudo pacman -S",
            "remove":   "sudo pacman -Rcsun",
            "update":   "sudo pacman -Sy",
            "notebook": "jupyter-notebook",
            "activate": "source ~/.venv/bin/activate",
        }

    def run(self):
        self._backup()
        self._add_aliases()

    def _backup(self):
        print("Backing up .bashrc...")
        subprocess.run([
            "tar", "-cvf", f"{self.home}/.bashrc.tar.gz",
            "-P", self.bashrc_path
        ])

    def _add_aliases(self):
        print("Adding aliases to .bashrc...")
        with open(self.bashrc_path, "a") as f:
            f.write(f"\n## Added by {self.username}\n")
            for alias, command in self.aliases.items():
                f.write(f"alias {alias}='{command}'\n")
        print("Done.")
