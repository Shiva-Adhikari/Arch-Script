# Built in Module
import os
import subprocess
import tempfile

# Local Module
from src.base import Base, load_config, logger
from src.package_manager import PackageManager


class AurPackage(Base):
    def __init__(self):
        config = load_config()
        self.aur_packages = config["aur"]
        self.dependencies = config["aur_dependencies"]
        self.services = config["aur_services"]
        self.paru_url = "https://aur.archlinux.org/paru-bin.git"

    def run(self):
        self._install_dependencies()
        self._install_paru()
        self._install_aur_packages()
        self._enable_services()

    def _install_dependencies(self):
        pm = PackageManager()
        pm.packages = self.dependencies
        pm.install_packages()

    def _install_paru(self):
        result = self._run_cmd(["pacman", "-Qq", "paru-bin"])
        if result.returncode == 0:
            logger.info("paru already installed, skipping...")
            return

        logger.info("Installing paru...")
        with tempfile.TemporaryDirectory() as tmpdir:
            result = subprocess.run(["git", "clone", self.paru_url], cwd=tmpdir)
            if result.returncode != 0:
                logger.error("Failed to clone paru-bin repository.")
                return
            result = subprocess.run(["makepkg", "-si"], cwd=os.path.join(tmpdir, "paru-bin"))
            if result.returncode != 0:
                logger.error("Failed to build and install paru.")
                return
        logger.info("paru installed.")

    def _install_aur_packages(self):
        logger.info("Installing AUR packages...")
        for package in self.aur_packages:
            result = self._run_cmd(["pacman", "-Qq", package])
            if result.returncode == 0:
                logger.info(f"{package} already installed, skipping...")
                continue

            logger.info(f"Installing {package}...")
            result = subprocess.run(["paru", "-S", "--noconfirm", package])
            if result.returncode != 0:
                logger.warning(f"Failed to install {package}")

    def _enable_services(self):
        pm = PackageManager()
        pm.enable_packages = self.services
        pm.enable_service()
