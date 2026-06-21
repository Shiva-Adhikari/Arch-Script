# Built in Module
import os
import subprocess

# Local Module
from src.base import Base, load_config, logger


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
                logger.warning("Invalid choice.")

    def _backup(self):
        logger.info("Backing up .bashrc...")
        result = subprocess.run([
            "tar", "-cJf", self.backup_path,
            "-P", self.bashrc_path
        ])
        if result.returncode == 0:
            logger.info(f"Backup saved to {self.backup_path}")
        else:
            logger.warning("Backup failed.")

    def _restore(self):
        if not os.path.exists(self.backup_path):
            logger.warning(f"No backup found at {self.backup_path}")
            return

        logger.info("Restoring .bashrc...")
        result = subprocess.run(["tar", "-xJf", self.backup_path, "-P"])
        if result.returncode == 0:
            logger.info("Restore complete.")
        else:
            logger.warning("Restore failed.")

    def _add_aliases(self):
        logger.info("Adding aliases to .bashrc...")
        try:
            with open(self.bashrc_path, "a") as f:
                f.write(f"\n## Added by {self.username}\n")
                for alias, command in self.aliases.items():
                    f.write(f"alias {alias}='{command}'\n")
            logger.info("Done.")
        except IOError as e:
            logger.error(f"Failed to write to .bashrc: {e}")
