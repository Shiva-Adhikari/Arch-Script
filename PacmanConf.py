import subprocess
class PacmanConf:
    def __init__(self):
        lines = [
            "\n",
            "[options]",
            "##Added By lx",
            "ParallelDownloads = 10",
            "ILoveCandy",
            "Color"
        ]
        for line in lines:
            subprocess.run(["sudo", "bash", "-c", f"echo '{line}' >> /etc/pacman.conf"])

if __name__ == '__main__':
    pacmanconf = PacmanConf()
