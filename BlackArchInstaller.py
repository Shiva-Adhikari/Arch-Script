import subprocess

class BlackArchInstaller:
    def install_black_arch(self):
        code = subprocess.run(["ls", "/etc/pacman.d/blackarch-mirrorlist"], capture_output=True, text=True)
        if code.returncode == 0:
            print("Already Installed...")
        else:
            print("Installing BlackArch packages...")
            subprocess.run(["sudo", "pacman", "-Syu"])
            subprocess.run(["sudo", "pacman", "-S", "curl", "--noconfirm"])
            subprocess.run(["curl", "-O", "https://blackarch.org/strap.sh"])
            subprocess.run(["chmod", "+x", "strap.sh"])
            subprocess.run(["sudo", "./strap.sh"])
            subprocess.run(["rm", "-rf", "strap.sh"])
            
            
if __name__ == '__main__':
    black_arch_installer = BlackArchInstaller()
    black_arch_installer.install_black_arch()
