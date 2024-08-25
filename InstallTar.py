import subprocess

class TarFile():
    def tar_file(self):
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "inetutils", "libxcrypt-compat", "net-tools"])
        
        print("Xampp")
        subprocess.run(["wget", "https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["chmod", "+x", "xampp-linux-x64-8.2.12-0-installer.run"])
        subprocess.run(["sudo", "./xampp-linux-x64-8.2.12-0-installer.run"])

if __name__ == "__main__":
    #packages= ["inetutils", "libxcrypt-compat", "net-tools"]
    tarfile = TarFile()
    tarfile.tar_file()
    #tarfile.install_packages(packages)
    
