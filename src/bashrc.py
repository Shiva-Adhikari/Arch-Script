# Built in Module
import os
import subprocess

# Local Module
from src.base import Base, load_config


class Bashrc(Base):
    def __init__(self):
        config = load_config()
        self.username = os.getenv("USER") or os.getenv("LOGNAME")
        self.home = os.path.expanduser("~")
        self.bashrc_path = f"{self.home}/.bashrc"
        self.backup_path = f"{self.home}/.bashrc.tar.xz"
        self.aliases = config["aliases"]

    def run(self):
        self._submenu()

    def _submenu(self):
        print("\n1. Add Aliases  → adds aliases from config to ~/.bashrc")
        print("2. Backup       → saves current ~/.bashrc to ~/.bashrc.tar.xz")
        print("3. Restore      → restores ~/.bashrc from backup")
        print("0. Back\n")

        choice = input("Enter Input: ").strip()
        match choice:
            case "1":
                self._add_aliases()
            case "2":
                self._backup()
            case "3":
                self._restore()
            case "0":
                return
            case _:
                print("Invalid choice.")

    def _backup(self):
        print("Backing up .bashrc...")
        subprocess.run([
            "tar", "-cJf", self.backup_path,
            "-P", self.bashrc_path
        ])
        print(f"Backup saved to {self.backup_path}")

    def _restore(self):
        if not os.path.exists(self.backup_path):
            print(f"No backup found at {self.backup_path}")
            return

        print("Restoring .bashrc...")
        subprocess.run(["tar", "-xJf", self.backup_path, "-P"])
        print("Restore complete.")

    def _add_aliases(self):
        print("Adding aliases to .bashrc...")
        with open(self.bashrc_path, "a") as f:
            f.write(f"\n## Added by {self.username}\n")
            for alias, command in self.aliases.items():
                f.write(f"alias {alias}='{command}'\n")
        print("Done.")
