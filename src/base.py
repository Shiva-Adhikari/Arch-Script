# Built in Module
import json
import logging
import os
import subprocess

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "packages.json")
LOG_PATH = os.path.expanduser("~/.arch-script.log")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("arch-script")


def load_config() -> dict:
    required_keys = [
        "pacman", "pacman_services", "aur", "aur_dependencies",
        "aur_services", "flathub", "uninstall", "bluetooth",
        "bluetooth_services", "ufw", "ufw_services", "aliases"
    ]
    try:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
    except FileNotFoundError:
        logger.error(f"Config file not found at {CONFIG_PATH}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config file: {e}")
        raise

    missing = [key for key in required_keys if key not in config]
    if missing:
        logger.error(f"Missing required keys in config: {', '.join(missing)}")
        raise KeyError(f"Missing keys: {', '.join(missing)}")

    return config


class Base:
    def run(self):
        raise NotImplementedError("Subclasses must implement run()")

    def _run_cmd(self, cmd: list) -> subprocess.CompletedProcess:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            logger.debug(f"Command {' '.join(cmd)} exited with code {result.returncode}")
        return result

    def _run_sudo(self, cmd: list) -> subprocess.CompletedProcess:
        result = subprocess.run(["sudo"] + cmd)
        if result.returncode != 0:
            logger.warning(f"sudo command failed: {' '.join(cmd)}")
        return result
