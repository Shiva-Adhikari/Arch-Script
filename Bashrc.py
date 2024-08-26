import subprocess

class Bashrc:
    # def __init__(self,aliases):
        # pass


    def add_aliases(self,aliases):
        self.aliases = aliases
# Backup the existing .bashrc file
        subprocess.run(["sudo", "tar", "-cvf", "/home/lx/.bashrc.tar.gz", "-P", "/home/lx/.bashrc"])

# Append aliases to the .bashrc file
        with open("/home/lx/.bashrc", "a") as f:
            f.write("\n## Added by lx\n")

            for alias, command in self.aliases.items():
                f.write(f"alias {alias}='{command}'\n")


if __name__ == '__main__':
    aliases = {
            "p": "paru",
            "s": "sensors",
            "py": "python",
            "search": "pacman Ss",
            "install": "sudo pacman -S",
            "remove": "sudo pacman -Rn",
            "update": "sudo pacman -Sy",
            "notebook": "jupyter-notebook",
            ".": "sudo create_ap wlan0 wlan0 .",
            "..": "sudo create_ap wlan0 wlan0 ..",
            "activate": "source ~/.venv/bin/activate",
            "xampp": "cd /opt/lampp/ && sudo ./manager-linux-x64.run",
            }
    
    bashrc = Bashrc()
    bashrc.add_aliases(aliases)
