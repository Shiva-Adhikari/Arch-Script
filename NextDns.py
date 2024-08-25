import subprocess
#import AurArchLinux

class NextDns():
    def next_dns(self):
        subprocess.run(["sudo", "nextdns", "install", "-profile", "e61fac", "-report-client-info", "-auto-activate"])
        subprocess.run(["sudo", "systemctl", "enable", "nextdns"])
        #subprocess.run(["sudo", "journalctl", "-u", "nextdns"])
        
        host = "127.0.0.1 localhost"
        subprocess.run(["sudo", "bash", "-c", f"echo '{host}' >> /etc/hosts"])
        
        main = "[main]"
        resolv = "systemd-resolved=false"
        subprocess.run(["sudo", "bash", "-c", f"echo '{main}' >> /etc/NetworkManager/conf.d/no-systemd-resolved.conf"])
        subprocess.run(["sudo", "bash", "-c", f"echo '{resolv}' >> /etc/NetworkManager/conf.d/no-systemd-resolved.conf"])
        
        subprocess.run(["systemctl", "enable", "systemd-resolved.service"])
        subprocess.run(["systemctl", "start", "systemd-resolved.service"])
        subprocess.run(["sudo", "systemctl", "restart", "nextdns"])
        subprocess.run(["sudo", "journalctl", "-u", "nextdns"])
        print("Done")

if __name__ == "__main__":    
    #aur_packages = { "nextdns-bin": "https://aur.archlinux.org/nextdns-bin.git" }
    #aur = AurArchLinux.AurArchLinux()
    #aur.install_aur_packages(aur_packages)

    nextdns = NextDns()
    nextdns.next_dns()
